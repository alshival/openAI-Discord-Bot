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
    
# Used to label the last prompt you sent. 
@bot.tree.command(name = "label_last")
@app_commands.choices(label=[
    app_commands.Choice(name = k, value = k) for k in keras_labels
    ])
async def label_last(interaction: discord.Interaction,label: app_commands.Choice[str]):
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
########################################################################
# Bot tasks
########################################################################
@tasks.loop(minutes=1)
async def reminders(bot):
    try:
        await update_reminders_table(bot)
        await send_reminders(bot)

    except Exception as e:
        print(f"Error in send_reminders: {e}")

@tasks.loop(minutes=90)
async def delete_downloads(bot):
    await delete_music_downloads(bot)
    print('Download folder cleared')
    
# 'on_ready' function is an event handler that runs after the bot has connected to the server.
# It starts the 'send_reminders' loop.
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    reminders.start(bot)
    delete_downloads.start(bot)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)    
bot.run(discord_bot_token)