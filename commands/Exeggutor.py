from app.config import *
from app.bot_functions import *

      
async def Exeggutor(ctx,python):
    
    extracted_code = extract_code(python) # Extract the code
    
    vars = {}
    # Save the original stdout so we can reset it later
    original_stdout = sys.stdout
    # Create a StringIO object to capture output
    captured_output = io.StringIO()
    # Redirect stdout to the StringIO object
    sys.stdout = captured_output

    try:
        code_compiled = compile(extracted_code,"<string>","exec") # Compiling code

        exec(code_compiled,vars,vars)  # execute the code    
    except Exception as e:
        jsonl = f"""
####################
Error
####################
```
{type(e).__name__} - {e}
```
"""
        await ctx.send(jsonl)
        print(f"Error: {type(e).__name__} - {e}")
        sys.stdout = original_stdout
    
        db_conn = await create_connection()
        await store_prompt(db_conn, ctx.author.name, f"""
Here's my python code:
```
{extracted_code}
```
Here's the error:
```
{e} 
```
""", openai_model, 'Noted.', ctx.channel.id,ctx.channel.name,'')
        await db_conn.close()
        return
    sys.stdout = original_stdout
    # Get the output
    output = captured_output.getvalue()
    print("done exegguting")
    jsonl = f'''
################################################################
Output:
################################################################
```
{output}
```
'''
    # check if there are any files
    strings =  [x for x in vars.values() if (type(x) is str)]
    files_to_send = [x  for x in strings if re.search('\.([^.]+$)',x) is not None]
    #send results
    await send_results(ctx,output,files_to_send)
    
    db_conn = await create_connection()
    await store_prompt(db_conn, ctx.author.name, f"""
Here's my python code:
```
{extracted_code}
```
Here's the output:
```
{output} 
```
""", openai_model, 'Noted.', ctx.channel.id,ctx.channel.name,'')
    await db_conn.close()