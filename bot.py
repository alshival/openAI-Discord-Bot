import discord
from discord.ext import commands,tasks
from discord import app_commands
from app.config import *


# Set up the bot with '!' as the command prefix. 
# It is set to listen and respond to all types of intents in the server. 
# You can change the command prefix by replacing '!' with your preferred symbol.
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

########################################################################
# Bot Boot Sequence
########################################################################
from app.bot_functions import *
from app.keras import tasks_layer
from app.fefe import *

# Create the prompts table if needed when the bot starts up
asyncio.get_event_loop().run_until_complete(create_prompts_table())
# Create the labeled_prompts table if needed when the bot starts up
asyncio.get_event_loop().run_until_complete(create_labeled_prompts_table())

# train the main keras layer
asyncio.get_event_loop().run_until_complete(tasks_layer.load_tasks_layer())

# Create the reminders table if needed when the bot starts up
asyncio.get_event_loop().run_until_complete(create_reminder_table())
# Load the reminders layer
#asyncio.get_event_loop().run_until_complete(load_reminder_layer())

########################################################################
# Bot Commands
########################################################################

@bot.command()
async def fefe(ctx,*,message: str):
    await talk_to_fefe(ctx,message,bot)

# V2 command
from commands.discord_interpreter import discord_interpreter
from commands.youtube import search_youtubev2
from commands.Data_Interpreter import Data_Interpreter
from commands.Exeggutor import Exeggutor
@bot.command()
@commands.has_permissions(administrator = True)
async def datalle(ctx,*,message: str):
    await Data_Interpreter.data_int(ctx,message,openai_model)

@bot.command()
@commands.has_permissions(administrator = True)
async def exeggutor(ctx,*,message: str):
    print("exegguting")
    await Exeggutor(ctx,message)
    
# Used to label the last prompt you sent. 
@bot.tree.command(name = "plugins")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.choices(
    plugin=[
        app_commands.Choice(name="interpreter",
                            value="interpreter"),
        app_commands.Choice(name="Search Youtube",value="search_youtube")
    ])
async def fefe_plugins(interaction: discord.Interaction, plugin: app_commands.Choice[str], message: str):
    
    await interaction.response.defer(thinking = True)
    
    if plugin.value == "interpreter":
        await discord_interpreter.discord_interpreter(interaction,message)
    elif plugin.value == "search_youtube":
        await search_youtubev2(interaction,message)

help_text = """
👋 Hi, I'm Fefe! I live on this server. 🍓🦄✨

🤖 I am an AI-powered Discord bot with market research analysis capabilities created by [Alshival's Data Service](https://www.alshival.com/ai-discord-bots)! 💖⭐️

🎶 Ask me to play music for you over voice channels and set reminders! ⏰🎵


📝 Here's a quick rundown on how to use the app:

 1️⃣ Talk to Fefe
- `!fefe <message>`: Chat with me. Ask me to set reminders, play music over the voice channel, or ask me questions about code or certain topics.
- `!datalle <message>`: Attach a `.csv` file and request charts be generated.
- `!exeggutor <python>`: Run raw python code.

2️⃣ There are also some slash commands that help:
- `/plugins Interpreter`: Use the Discord interpreter to execute Python code.
- `/label_last <label>`: Label the last prompt you sent to retrain me if I don't understand you.
- `/clear_reminders`: Clear all your reminders.
- `/retrain_keras`: Retrain the Keras layer (Admins only).
- `/stop_music`: Stop music playback in voice channels.
- `/upgrade_fefe`: Upgrade me.
- `/restart_fefe`: Restart me.

💼 If you're into finance, try using the Discord Interpreter at `/plugins Interpreter <message>` to generate stock market charts! 📈📉

You can ask me questions about code produced by `!datalle`, `!exeggutor`, and the Discord interpreter at `/plugins Interpreter` using `!fefe`. I will be happy to provide further assistance and explanations.

📚 You can grab the code and instructions needed to install me on your server by visiting our site. We can also customize the app and the AI for your server.

🚀 Join the fun and make the most of your Discord experience! If you have any questions or need help, feel free to reach out. 😄

Experience the power of data with Alshival's Data Service. 🍉🌟💕
"""

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    embed1 = discord.Embed(
            color = discord.Color.orange()
        )
    embed1.set_author(name=f"{interaction.user.name} asked for help.",icon_url=interaction.user.avatar)
    
    await interaction.response.send_message(help_text,embed=embed1)
    
# Used to label the last prompt you sent. 
@bot.tree.command(name = "label_last")
@app_commands.choices(label=[
    app_commands.Choice(name = k, value = k) for k in keras_labels
    ])
async def label_last(interaction: discord.Interaction,label: app_commands.Choice[str]):
    await interaction.response.defer(thinking = True)
    await label_last_prompt(interaction,label.value)

# '!clear_reminders` command 
@bot.tree.command(name="clear_reminders")
async def clear_reminders(interaction: discord.Interaction):
    await clear_user_reminders(interaction)

# '!retrain_keras' command to retrain the model. Must be run by an administrator.
@bot.tree.command(name="retrain_keras")
@app_commands.checks.has_permissions(administrator=True)
async def retrain_keras(interaction: discord.Interaction):
        await interaction.response.send_message('Training. Standby...')
        await tasks_layer.train_tasks_layer()
        await interaction.followup.send('Training complete.')
    
# this command stops the bot from playing music
@bot.tree.command(name="stop_music")
async def stop_music(interaction: discord.Interaction):
    voice_state = interaction.user.voice
    if voice_state is None or voice_state.channel is None:
        await interaction.response.send_message("You are not connected to a voice channel.")
        return

    voice_channel = voice_state.channel
    voice_client = interaction.guild.voice_client
    #voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_connected() and voice_client.channel == voice_channel:
        await voice_client.disconnect()
        await interaction.response.send_message("Music playback stopped.")
    else:
        await interaction.response.send_message("The bot is not currently playing any music.")

def restart_bot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@bot.tree.command(name="restart_fefe")
@app_commands.checks.has_permissions(administrator=True)
async def restart_fefe(interaction: discord.Interaction):
    await interaction.response.send_message("Restarting bot...")
    restart_bot()
    
@bot.tree.command(name="upgrade_fefe")
@app_commands.checks.has_permissions(administrator=True)
async def upgrade_fefe(interaction: discord.Interaction):
    embed1 = discord.Embed(
            color = discord.Color.gold()
        )
    embed1.set_author(name=f"{interaction.user.name} upgraded Fefe",icon_url=interaction.user.avatar)
    
    await interaction.response.defer(thinking = True)
    
    import subprocess

    # Save the original stdout so we can reset it later
    original_stdout = sys.stdout
    # Create a StringIO object to capture output
    captured_output = io.StringIO()
    # Redirect stdout to the StringIO object
    sys.stdout = captured_output

    command = ['git','pull','origin','main']
    result = subprocess.run(command, capture_output=True, text = True)
    jsonl = f"""
```
{result.stdout}
```
"""
    await interaction.followup.send(jsonl,embed=embed1)
    await interaction.followup.send("Restarting bot...")
    restart_bot()
    
########################################################################
# Bot tasks
########################################################################
reminder_task_loop_running = False
@tasks.loop(minutes=1)
async def reminders(bot):
    global reminder_task_loop_running
    reminder_task_loop_running = True
    try:
        await update_reminders_table(bot)
        await send_reminders(bot)

    except Exception as e:
        print(f"Error in send_reminders: {e}")

delete_downloads_task_loop_running = False
@tasks.loop(minutes=90)
async def delete_downloads(bot):
    global delete_downloads_task_loop_running
    delete_downloads_task_loop_running = True
    await delete_music_downloads(bot)
    print('Download folder cleared')
    
# 'on_ready' function is an event handler that runs after the bot has connected to the server.
# It starts the 'send_reminders' loop.
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    if not reminder_task_loop_running:
        reminders.start(bot)
    if not delete_downloads_task_loop_running:
        delete_downloads.start(bot)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)    
    
    first_text_channel = await list_text_channels(bot)
    
    await first_text_channel.send("I'm online! :heart:")  # Post a message in the first text channel
        
bot.run(discord_bot_token)