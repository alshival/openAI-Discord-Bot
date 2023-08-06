from app.config import *
from app.bot_functions import *
import io
import sys
      
async def Exeggutor(ctx,python):
    
        extracted_code = extract_code(python) # Extract the code
        
        code_compiled = compile(extracted_code,"<string>","exec") # Compiling code

        vars = {}
        # Save the original stdout so we can reset it later
        original_stdout = sys.stdout
        # Create a StringIO object to capture output
        captured_output = io.StringIO()
        # Redirect stdout to the StringIO object
        sys.stdout = captured_output
    
        try:
            exec(code_compiled,vars,vars)  # execute the code    
            # Reset stdout to its original value
            sys.stdout = original_stdout
        except Exception as e:
            await ctx.send(f"""
####################
Error
####################
```
{type(e).__name__} - {e}
```
""")
            # Reset stdout to its original value
            sys.stdout = original_stdout
            print(f"Error: {type(e).__name__} - {e}")
            return
        
        # Get the output
        output = captured_output.getvalue()
        print("done exegguting")
    
        # check if there are any files
        strings =  [x for x in vars.values() if (type(x) is str)]
        files_to_send = [x  for x in strings if re.search('\.([^.]+$)',x) is not None]
        #files_to_send = []
        if len(files_to_send)>0:
            await ctx.send(f'''
####################
Output
####################
```
{output}
```
''',files = [discord.File(x) for x in files_to_send])  # get the output from the buffer
        else:
            await ctx.send(f'''
####################
Output
####################
```
{output}
```
    ''')
            return
                           
