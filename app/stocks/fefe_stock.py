from app.config import *
import matplotlib.pyplot as plt
import yfinance as yf
from app.stocks import sample_prompts
from app.bot_functions import *

async def stock(ctx,message,model,db_conn):
    filename = f"app/stocks/{ctx.author.name}.png"
    py_filename = f"app/stocks/{ctx.author.name}.py"
    
    await store_prompt(db_conn, ctx.author.name, message, model, '', ctx.channel.name,keras_classified_as='stock-chart')
    
    messages = sample_prompts.sample_prompts[2:5]
    messages.append({'role': 'user', 'content': 'Do not change the line `filename=filename`. If you decide to use a dark theme, set it using `plot.style.use(\'dark_background\')`:' + message})
     
        # Generate a response using the 'gpt-3.5-turbo' model
    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=1024,
            n=1,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
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
        response_compiled = compile(extracted_code,"<string>","exec")
        exec(response_compiled)
        # Send the .png file as a message to the user
        await ctx.send(file=discord.File(filename))
        # Send the code used to generate the chart to the user
        jsonl = f'''
{{'role':'user','content':"""{message}"""}},
{{'role':'assistant','content':f"""\n{extracted_code}\n"""}}'''
        # Open the file in write mode and save the list of dictionaries as a JSON Lines file
        with open(py_filename, 'w') as file:
            file.write(jsonl)
        await ctx.send(file=discord.File(py_filename))
        # Remove the locally saved .png file
        os.remove(py_filename)
        
    except Exception as e:
        print(message)
        print(e)
        print(extracted_code)
        await ctx.send(f"Sorry... I had a bit of an issue generating that chart. Might have tried to use a package that is not locally installed or something that didn't work: \n {e}")
        # Send the code that gave the error
        with open(py_filename, "w") as file:
            file.write(f'''
################
Error:
'{e}'
################
{{'role':'user','content':'{message}'}},
{{'role':'assistant','content':
"""
{extracted_code}
"""}}'''
                      )
        await ctx.send(file=discord.File(py_filename))
        # Remove the locally saved .png file
        os.remove(filename)
        return
    # Store the new prompt and response in the 'prompts' table
    await store_prompt(db_conn, ctx.author.name, message, model, response_text, ctx.channel.name,keras_classified_as='stock-chart')
    await db_conn.close()
