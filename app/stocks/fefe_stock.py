from app.config import *
import matplotlib.pyplot as plt
import yfinance as yf
from app.stocks import finetune_data
from app.bot_functions import *

async def stock(ctx,message,model,db_conn):
    py_filename = f"app/stocks/{ctx.author.name}.py"
    await store_prompt(db_conn, ctx.author.name, message, model, '', ctx.channel.id,ctx.channel.name,keras_classified_as='stock-chart')
    
    # messages = finetune_data.finetune[0:4]
    # For random prompts.
    messages = [[finetune_data.finetune[i],finetune_data.finetune[i+1]] for i in [j for j in range(len(finetune_data.finetune)) if j%2==0]]
    messages = random.sample(messages,sample_stock_charts) # sample_stock_charts defined in `app/config.py`.
    messages = [item for sublist in messages for item in sublist]

    messages.append({'role': 'user', 'content': f'Save the image as a .png. If you decide to use a dark theme, set it using `plot.style.use(\'dark_background\')`:' + message})
    try: 
        # Generate a response using the 'gpt-3.5-turbo' model
        response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=1450,
                n=1,
                temperature=0.5,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.4,
            )
    except Exception as e:
        ctx.send(f"Sorry! Had an issue with the openAi API: \n {type(e).__name__} - {str(e)}")
        return
    # Extract the response text and send it back to the user
    response_text = response['choices'][0]['message']['content']
    if '`' in response_text:
        pattern = r"```(?:[a-z]*\s*)?(.*?)```\s*"
        match = re.search(pattern, response_text, re.DOTALL)
        if match:
            extracted_code = match.group(1) # Get the content between the tags
            print(extracted_code)
    elif 'import' in response_text:
        extracted_code = response_text
    else:
        extracted_code = response_text
        print("No code found.")
    try:
        global_vars = globals().copy()
        global_vars['ctx'] = ctx
        response_compiled = compile(extracted_code,"<string>","exec")
        exec(response_compiled,global_vars)
        # Send the .png file as a message to the user
        await ctx.send(file=discord.File(global_vars['filename']))
        # Send the code used to generate the chart to the user
        jsonl = f'''{{'role':'user','content':"{r'' +message}"}},
{{'role':'assistant','content':"""\n{extracted_code}\n"""}}'''
        # Open the file in write mode and save the list of dictionaries as a JSON Lines file
        
        with open(py_filename, 'w') as file:
            file.write(jsonl)
        await ctx.send(file=discord.File(py_filename))
        # Remove the locally saved .png file
        os.remove(global_vars['filename'])
        
    except Exception as e:
        print(message)
        print(e)
        print(extracted_code)
        await ctx.send(f"Sorry... I had a bit of an issue generating that chart. Might have tried to use a package that is not locally installed or something that didn't work: \n {e}")
        # Send the code that gave the error
        with open(py_filename, "w") as file:
            file.write(f'''
################################################################
Error:
{type(e).__name__} - {str(e)}
################################################################
{{'role':'user','content':'{message}'}},
{{'role':'assistant','content':
"""
{extracted_code}
"""}}'''
                      )
        await ctx.send(file=discord.File(py_filename))
        return
    # Store the new prompt and response in the 'prompts' table
    await store_prompt(db_conn, ctx.author.name, message, model, response_text, ctx.channel.id,ctx.channel.name,keras_classified_as='stock-chart')
    await db_conn.close()
