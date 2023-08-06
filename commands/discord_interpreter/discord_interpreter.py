from commands.discord_interpreter import finetune_data
import yfinance as yf
import matplotlib.pyplot as plt
from app.config import *

async def discord_interpreter(interaction, message):
    embed1 = discord.Embed(
            description = message,
            color = discord.Color.purple()
        )
    embed1.set_author(name=f"{interaction.user.name} used the Discord Interpreter",icon_url=interaction.user.avatar)
    
    py_filename = f"app/{interaction.user.name}.py"

    messages = [[finetune_data.finetune[i],finetune_data.finetune[i+1]] for i in [j for j in range(len(finetune_data.finetune)) if j%2==0]] 

    # Random sample messages.
    messages = random.sample(messages,sample_stock_charts)
    # sample_stock_charts defined in `app/config.py`.

    messages = [item for sublist in messages for item in sublist]

    messages.append({'role': 'user', 'content': f'Use the same standardized code format as before. Save the file using the variable `filename`:' + message})

    try:
        response = openai.ChatCompletion.create(
            model=openai_model,
            messages=messages,
            max_tokens=1450,
            n=1,
            temperature=0.6,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            user = interaction.user.name
        )
    except Exception as e:

        messages.append({'role':'user','content':f'I have an error: {type(e).__name__} - {str(e)}'})
        # Give them the opportunity to try again
        response = openai.ChatCompletion.create(
                model = openai_model,
                messages = messages,
                max_tokens = 1450,
                n = 1,
                temperature = 0.5,
                top_p = 1,
                frequency_penalty = 0.0,
                presence_penalty = 0.4
            )
        interaction.followup.send(f"Mmm. I tried something, but it didn't work. Let's try again. \n \n Error: {type(e).__name__} - {str(e)}",embed=embed1)
        return
    # Extract the resopnse text and send it back to the user
    response_text = response['choices'][0]['message']['content']

    if '`' in response_text:
        extracted_code = extract_code(response_text)
    elif 'import' in response_text:
        extracted_code = response_text
    else:
        extracted_code = response_text
        print("No code found")
    try:
        vars = {}
        response_compiled = compile(extracted_code,"<string>","exec")
        exec(response_compiled, vars,vars)
        strings =  [x for x in vars.values() if (type(x) is str)]
        files_to_send = [x  for x in strings if re.search('\.([^.]+$)',x) is not None]
        # Send the zcode back to the user
        jsonl = f'''{{'role':'user','content':"{r'' +message}"}},
{{'role':'assistant','content':"""\n{extracted_code}\n"""}}'''
        with open(py_filename, 'w') as file:
            file.write(jsonl)
        # Send the .png file back
        await interaction.followup.send(files=[discord.File(x) for x in files_to_send] + [discord.File(py_filename)],embed=embed1)
        # delete locally saved .png file
        for file in files_to_send:
            os.remove(file)
    except Exception as e:
        print(message)
        print(e)
        print(extracted_code)
        await interaction.followup.send(f"Sorry... I had a bit of an issue generating that chart. Might have tried to use a package that is not locally installed or something that didn't work: \n {e}")
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
            
        await interaction.followup.send(file=discord.File(py_filename),embed=embed1)