from app.config import *
from app.bot_functions import *
from app.keras import tasks_layer
import requests
import pandas
# For creating reminders
from app.reminders.fefe_reminders_openai import *
# For general discussion
from app.fefe_openai import *
# For searching youtube
from app.fefe_youtube import *

# Interaction_version
async def GPT(interaction,message):
    embed1 = discord.Embed(
        description = message,
        color = discord.Color.purple()
    )
    embed1.set_author(name=f"{interaction.user.name} used {openai_model}",icon_url=interaction.user.avatar)
    
    db_conn = await create_connection()
    
    past_prompts = await fetch_prompts(db_conn,interaction.channel.name,4)
    messages = []
    # Add past prompts from `data.db`
    for prompt, response in past_prompts:
        messages.extend([{'role': 'user', 'content': prompt}, {'role': 'assistant', 'content': response}])
    # Add latest message
    messages.append({'role': 'user', 'content': message})

    # Generate a response using the 'gpt-3.5-turbo' model
    response = openai.ChatCompletion.create(
        model=openai_model,
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

    # respond to slash command
    embed = discord.Embed(
        description = message,
        color = discord.Color.red())
    embed.set_author(name=f"@{interaction.user.name}",icon_url=interaction.user.avatar)
    await send_chunks_interaction(interaction,response_text,embed=embed1)
    await store_prompt(db_conn,
                 interaction.user.name,
                 message,
                 openai_model,
                 response_text,
                 interaction.channel_id,
                 interaction.channel.name,
                 keras_classified_as = '')
    await db_conn.close()