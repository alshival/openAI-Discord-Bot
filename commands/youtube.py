from app.config import *
from app.bot_functions import *

async def search_youtubev2(interaction, message):
    try:
        search_response = youtube.search().list(
            q = message,
            part = "id,snippet",
            maxResults = 3
        ).execute()
        # Create a formatted string with the video titles
        video_titles = "\n".join(
            f"""[{search_result["snippet"]["title"]}](https://www.youtube.com/watch?v={search_result["id"]["videoId"]})"""
            for search_result in search_response.get("items", [])
            if search_result["id"]["kind"] == "youtube#video"
        )

        response = openai.ChatCompletion.create(
            model = openai_model,
            messages = [
                {'role':'user','content': "Cupid by Fifty Fifty"},
                {'role':'assistant','content':f'Of course, ❤️{interaction.user.mention}❤️. But you don\'t need cupid.'},
                {'role':'user','content':"How do I integrate over a line in the complex numbers?"},
                {'role':'assistant','content':f"I got you,, {interaction.user.mention}. ❤️💕 I home we aren't as complicated."},
                {'role':'user','content':'Importing a csv file into python'},
                {'role':'assistant','content':f'Sure thing, {interaction.user.mention}❤️🍇. Are you a parseltongue if you can speak python?'},
                {'role':'user','content':f'Generate a short reply like the previous ones. Tease them a bit:'+ message}
            ],
            n = 1,
            temperature = 0.25,
            top_p = 1
        )
        response_text = response['choices'][0]['message']['content']
        
        # Send the video titles as a message in the Discord channel
        embed = discord.Embed(
            description = message,
            color = discord.Color.teal()
        )
        embed.set_author(name=f"{interaction.user.name} searched YouTube.",icon_url=interaction.user.avatar)
    
        await interaction.followup.send(response_text + '\n\n' + video_titles,embed = embed)

    except HttpError as e:
        await interaction.followup.send(f"Sorry, there appears to have been an issue when searching: \n \n{e}")
        print("An HTTP error occurred:")
        print(e)

#These are options for the youtube dl, not needed actually but are recommended
ytdlopts = { 
    'format': 'bestaudio/best',
    'outtmpl': 'app/downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  
    'force-ipv4': True,
    'preferredcodec': 'mp3',
    'cachedir': False
    
    }

ffmpeg_options = {
        'options': '-vn'
    }

ytdl = yt_dlp.YoutubeDL(ytdlopts)

async def play_youtube(interaction,message):
    embed = discord.Embed(
            description = message,
            color = discord.Color.purple()
        )
    embed.set_author(name=f"{interaction.user.name} used Discord Interpreter",icon_url=interaction.user.avatar)
    
    user_voice = interaction.user.voice
    if user_voice is None:
        print(interaction.user)
        await interaction.followup.send("Join a voice channel first then ask me again.",embed = embed)
        return

    voice_client = user_voice.channel
    voice = await voice_client.connect()
    # Search Youtube
    try:
        search_response = youtube.search().list(
            q = message,
            part = "id,snippet",
            maxResults = 1
        ).execute()
        search_result = [x for x in search_response.get("items",[]) if x["id"]["kind"] == "youtube#video"][0]
        video_url = f"""https://youtu.be/{search_result["id"]["videoId"]}"""
        video_title = f"""### {search_result["snippet"]["title"]}"""
    except Exception as e:
        await interaction.followup.send("Sorry! I had an issue pulling results from youtube. Nothing came back.",embed=embed)
        return
        
    loop = asyncio.get_event_loop()
    
    # Download the youtube video data
    data = await loop.run_in_executor(None,lambda: ytdl.extract_info(url=video_url,download = True))

    title = data['title']
    song = data['url']
    print(data['url'])
    if 'entries' in data:
        data = data['entries'][0]
    try:
        voice_client.play(discord.FFmpegPCMAudio(source=song,**ffmpeg_options, executable="ffmpeg"))
    except Exception as e:
        await interaction.followup.send(f"Had an issue connecting: {e}",embed=embed)

    await interaction.followup.send(f"### Playing: {title}\n{video_url}")
    