from app.config import *
from app.bot_functions import *
# We need to produce code to execute. Either to set a reminder or to look up a remind. The Ai will be taught to do both.
from app.reminders import finetune_data

async def reminder(ctx,message,model,db_conn):
    py_filename = f"app/reminders/{ctx.author.name}.py"
    return_py_file = False
    sample_prompts = finetune_data.finetune
    sample_prompts.append({'role':'user','content':f'Write code like before for this request: \n```\n{message}\n```\n".'})

    response = openai.ChatCompletion.create(
        model = model,
        messages=sample_prompts,
        max_tokens = 1450,
        n = 1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    response_raw = response['choices'][0]['message']['content']
    if '`' in response_raw:
        pattern = r"```(?:[a-z]*\s*)?(.*?)```\s*"
        match = re.search(pattern, response_raw, re.DOTALL)
        if match:
            extracted_code = match.group(1)
    elif 'import' in response_raw:
        extracted_code = response_raw
    else:
        print("No code found.")
        print(response_raw)
        await ctx.send("Sorry. Having issues completing that request.")
        if return_py_file:
            jsonl = f'''{{'role':'user','content':"{r'' +message}"}},
{{'role':'assistant','content':"""\n{response_raw}\n"""}}'''
            with open(py_filename, 'w') as file:
                file.write(jsonl)
            await ctx.send(file=discord.File(py_filename))
            # Remove the locally saved .png file
            os.remove(py_filename)
            return
    try:
        response_compiled = compile(extracted_code,"<string>","exec")
        # Define the dictionary for globals()
        global_vars = globals().copy()
        global_vars['ctx'] = ctx
        exec(response_compiled,global_vars)
        # Send the response_text variable defined in the compiled code (See training examples):
        if global_vars['reminder_dict']:
            await add_reminder(*global_vars['reminder_dict'])
            await ctx.send(global_vars['response_text'])
        else:
            await ctx.send("Mhmm... I'm sorry... I had trouble understanding. Can you rephrase it for me?")
        jsonl = f'''{{'role':'user','content':"{r'' +message}"}},
    {{'role':'assistant','content':"""\n{extracted_code}\n"""}}'''
        if return_py_file:
            with open(py_filename, 'w') as file:
                file.write(jsonl)
            await ctx.send(file=discord.File(py_filename))
            # Remove the locally saved .png file
            os.remove(py_filename)
    except Exception as e:
        await ctx.send(f"Sorry... I had a bit of an issue setting that reminder... If I completely misunderstood you and you weren't asking to set a reminder, label your last prompt using `!label_last` as either `stock-chart`, `youtube`, or `other`.\n \n Error: {e}")

        jsonl = f'''
################################################################
Error: {type(e).__name__} - {str(e)}
################################################################
{{'role':'user','content':'{message}'}},
{{'role':'assistant','content':
"""
{extracted_code}
\n"""}}'''

        # Send the code that gave the error
        with open(py_filename, "w") as file:
            file.write(jsonl)
        await ctx.send(file=discord.File(py_filename))
        # Remove the locally saved .png file
        os.remove(py_filename)
        
# Store the new prompt and response in the 'prompts' table
    await store_prompt(db_conn, ctx.author.name, message, model, jsonl, ctx.channel.id,ctx.channel.name,keras_classified_as='reminder')
    await db_conn.close()