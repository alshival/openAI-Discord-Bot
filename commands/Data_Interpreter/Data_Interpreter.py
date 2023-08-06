from app.config import *
import matplotlib.pyplot as plt
import yfinance as yf
import re
import requests
import pandas
from commands.Data_Interpreter import finetune_data
from app.bot_functions import *

async def data_int(ctx,message,model):

    py_filename = f"app/downloads/{ctx.author.name}.py"
    #filename = f'app/downloads/{ctx.author.name}.png'

    # Check if there is a .csv file attached.
    if len(ctx.message.attachments)==1:
        url = ctx.message.attachments[0].url
        print(url)
        # get filename using regex
        filename = re.search('([^\/]+$)',url).group(0)
        filepath = 'app/downloads/' + re.search('([^\/]+$)',url).group(0)
        filetype = re.search('\.([^.]+$)',url).group(0)
        
        res = requests.get(url)
        # Extract file type
        with open(filepath,'wb') as file:
            file.write(res.content)
        print("Attachment downloaded successfully!")
    else: 
        ctx.send("Attach a file to continue")
        return
    
    # For random prompts.
    messages = finetune_data.finetune
    # Prepare the prompt for OpenAI by displaying the user message and the data column types
    if filetype == '.csv':
        data = pd.read_csv(filepath)
    prompt_prep = f"""
filename:
```
{filename}
```

columns:
```
{data.dtypes}
```

request:
```
{message}
```
"""
    
    messages.append({'role': 'user', 'content': f'If you decide to use a dark theme using matplotlib, set it using `plot.style.use(\'dark_background\')`: \n' + prompt_prep})
    
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
    # Extract the response text
    response_text = response['choices'][0]['message']['content']
    extracted_code = extract_code(response_text)
    response_compiled = compile(extracted_code, "<string>", "exec")
    
    # Create a copy of the global variables and set the 'data' variable to the provided DataFrame
    global_vars = globals().copy()
    global_vars['data'] = data
    try:
        # Execute the extracted code with the global variables
        exec(response_compiled, global_vars)
        jsonl = f'''
{{'role':'user','content':"""\n{prompt_prep}\n"""}},
{{'role':'assistant','content':"""\n{extracted_code}\n"""}}'''
    
        with open(py_filename, 'w') as file:
            file.write(jsonl)
        
        await ctx.send(files=[discord.File(global_vars['filename']),discord.File(py_filename)])

    except Exception as e:
        print(e)
