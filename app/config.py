import os
import pickle
import discord
from discord.ext import commands,tasks
import re
import random
import traceback

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
openai.api_key = os.environ.get("OPENAI_API_KEY")

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
from datetime import datetime, timedelta
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
keras_labels = ['other', 'reminder', 'stock-chart','youtube']

feature_display_text = """
`!label_last reminder` - If your request was about a reminder.
`!label_last youtube` - For youtube requests.
`!label_last stock-chart` - If you wanted me to generate a stock market chart for you.
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