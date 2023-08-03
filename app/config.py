import os
import pickle
import discord
from discord.ext import commands,tasks
import re
import random
import traceback
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# Set up Discord Bot token here:
discord_bot_token = os.environ.get("DISCORD_BOT_TOKEN")

import pandas as pd
import math
from datetime import datetime, timedelta
import json
############################################
# openai API config 
############################################
import openai
# Set up the OpenAI API. The key is stored as an environment variable for security reasons.
openai_model = 'gpt-3.5-turbo'
openai.api_key = os.environ.get("OPENAI_API_KEY")
sample_stock_charts = 4

############################################
# Youtube Data API config
############################################
import yt_dlp
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# Set up the Google Youtube Data API key. For youtube searching and playback.
google_api_key = os.environ.get("google_api_key")

# Set up the YouTube Data API client
youtube = build("youtube", "v3", developerKey=google_api_key)

############################################
# Stocks config
############################################
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.dates as mdates
#############################################
# KERAS LAYER - Task Assignment
#############################################
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import Input, Embedding, Dense, GlobalMaxPooling1D, Dot, Activation, Softmax, Multiply
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.layers import Flatten
from keras.models import load_model
# Number of training epochs for the keras layer.
epochs = 20
# Path to GloVe embedding used by the keras layer.
GloVe = 'app/glove.6B/glove.6B.100d.txt'

# Define the labels for task assignment in the Keras model
keras_labels = ['other', 'reminder','youtube']

feature_display_text = """
`!label_last reminder` - If your request was about a reminder.
`!label_last youtube` - For youtube requests.
`!label_last other` - For all other requests.
"""

# Note for developers:
# When adding new features that require task assignment in the Keras model,
# make sure to update this list of labels accordingly in conjunction with the changes made in app/keras_layer.py.

############################################
# database config
############################################
import sqlite3
import aiosqlite
import asyncio

# Where you wish to store the bot data.
db_name = 'app/data.db'

# Number of prompts stored in the local SQLite database. The table is truncated when the bot starts up.
prompt_table_cache_size = 200

# This function establishes a global connection to the 'data.db' SQLite database.
# It is used by some other functions whenever they need to interact with the database.
async def create_connection():
    return await aiosqlite.connect(db_name)

############################################
# Useful Functions
############################################
# Used to abide by Discord's 2000 character limit.
async def send_chunks(ctx, text):
    chunk_size = 2000  # Maximum length of each chunk

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    for chunk in chunks:
        await ctx.send(chunk)
async def send_chunks_interaction(interaction, text, embed =[]):
    if embed == []:
        embed = discord.Embed(
            description = text,
            color = discord.Color.red()
        )
        embed.set_author(name=f"@{interaction.user.name}",icon_url=interaction.user.avatar)
    chunk_size = 2000  # Maximum length of each chunk

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    if len(chunks) == 1:
        await interaction.followup.send(chunks[0],embed=embed)
    else:
        for chunk in chunks:
            if chunk == chunks[0]:
                await interaction.followup.send(chunk)
                
            if chunk != chunks[len(chunks)-1]:
                await interaction.followup.send(chunk)
            else:
                await interaction.followup.send(chunk,embed=embed)