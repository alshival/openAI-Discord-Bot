# openAi Discord Bot with Market Research Analysis
Demo: [Vimeo](https://vimeo.com/845117509)

This Discord bot utilizes OpenAi's `gpt-3.5-turbo` model and provides additional functionalities like setting reminders, playing music with the help of a sqlite database, a keras layer, and Google's Youtube. It now also includes a Market Research Analysis feature, which allows you to create financial charts using yfinance and mix charts with regression lines.

Created by [Alshival's Data Service](https://alshival.com) to enhance your Discord server experience. Whether it's for personal use, a group of friends, a study group, or project management, this bot has got you covered.

Note that the Discord Interpreter creates a server vulnurability, since it depends on the `exec` function. You can spit the output of `.bashrc`, revealing security keys by creating a prompt. Essentially, the Ai can access all files in a sandbox. This is why Discord Interpreter is aimed for small study groups and small teams. It works very well in a virtual environment or on a dedicated raspberry pi.

Study groups can benefit from a Discord bot that utilizes OpenAI's GPT models. It can set reminders, play music, and create financial charts using natural language. Since Ai can make mistakes, the python code used to generate the charts is returned within a python dictionary suitable for fine-tuning an openAi model for better performance.  

This version of the bot utilizes GPT3.5. Feel free to use this code as inspiration for utilizing newer models, such as GPT4, or reach out to us at [support@alshival.com](mailto:support@alshival.com). 

<html>
<body>
    <table style="width: 100%;" cellspacing="0" cellpadding="0">
        <tr>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Screenshot%202023-08-04%207.43.52%20AM.png?raw=True" alt="Image Description">
            </td>
            <td style="width: 50%;">
                <img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Screenshot%202023-08-04%207.43.58%20AM.png?raw=True" alt="Image Description">
            </td>
        </tr>
        <tr>
            <td style="width: 100%;">
                <img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Stock_Prices_5_Years.png?raw=True" alt="Image Description">
            </td>
        </tr>
    </table>
</body>
</html>

## Usage

- Use the command prefix `!` to interact with the bot:

  - `!fefe <message>`: Ask Fefe questions, set reminders, play music over a voice channel, or to write code and search for answers.
- The bot also includes the following slash commands:
  - `/gpt <plugin> <message>': Ask Fefe to generate financial charts.
  - `/help`: Provides a quick rundown of how to use the app.
  - `/label_last <label>`: Label the last prompt you sent to retrain the bot, in the event that she misunderstands your request.
  - `/retrain_keras`: Retrain the Keras layer after labeling prompts using `/label_last`. (Only accessible to server administrators)
  - `/clear_reminders`: Clear all reminders set by the user.
  - `/stop_music`: Used to stop music playback in voice channels.

## Features

- Chat with the bot using OpenAI's GPT models
- Ask the bot to set reminders for you.
- Ask the bot to play music through voice channels.
- Perform Market Research Analysis using yfinance to create financial charts and mix charts with regression lines.

The LLM we are using was better at writing matplotlib code than they were plotnine or plotly code. A newer LLM, such as GPT4 or Llama2, may be able to write plotly code more accurately

If you have GPT-4, you can adjust the code to use GPT4 in `app/fefe_openai.py` and `app/stocks/fefe_stocks.py` to use that model. You can include more sample training data along with your prompt if you use GPT4, as the token limit is higher than GPT3.5's. This should improve results. For stock charts, sample data used for generation is located at `app/stocks/finetune_data.py`. You can include any charts you like that the bot produces in the openAi training data (not to be mistaken with the keras training data, which is kept in `data.db` under the `prompts` table. More on that later.), which at the moment is a manual copy/paste process. You can adjust the number of sample prompt/chart pairs passed to openAi when generating a stock in the config file under the openAi section:
```
############################################
# openai API config 
############################################
import openai
# Set up the OpenAI API. The key is stored as an environment variable for security reasons.
openai.api_key = os.environ.get("OPENAI_API_KEY")
sample_stock_charts = 4
```

Discord servers can leverage an OpenAI-powered bot for code assistance, troubleshooting, generating financial charts, and answering technical questions. Discord servers centered around creative writing, storytelling, or roleplaying can use a bot with OpenAI's GPT models to generate prompts, develop characters, and facilitate interactive storytelling experiences. Gaming communities can incorporate an OpenAI-powered bot into their Discord server to provide in-game tips, strategies, and assist with game-related queries.

# Installation
### Set up bot on Discord
- Set up your bot on the [Discord Developer Portal](https://discord.com/developers/applications) and invite it to your server.
- In the bot's settings, you can customize various options such as its username, profile picture, and permissions. Make sure to at least enable the "Presence Intent" and "Server Members Intent" if your bot requires them.
- Under the "Token" section, click on the "Copy" button to copy your bot token. This token is

### Set environmental variables
- Set the environmental variables referenced in `app/config.py`:

   - `DISCORD_BOT_TOKEN`
   - `OPENAI_API_KEY`
   - `google_api_key` (Need Youtube Data API enabled for music playback)
### Clone Repository
- Clone the repository:

   ```shell
   gh repo clone alshival/openAi-Discord-Bot
   ```

### Install the required dependencies:
We suggest installing the bot's python dependencies in a virtual environment. You will need ffmpeg on your system to play music via the voice channel: `sudo apt install ffmpeg`.
To install on a linux machine or linux subsystem:

  - Navigate to the directory where your `requirements.txt` file is located:
     ```shell
     cd /path/to/your/openAi-Discord-Bot/
     ```
     
  - Create and activate the virtual environment:
     ```
     python3 -m venv env
     source env/bin/activate
     ```

  - Run the following command to install the packages:
     ```shell
     pip3 install -r requirements.txt
     deactivate # deactivates the virtual environment
     ```
   
Wait for the installation to complete. Pip will read the `requirements.txt` file and automatically download and install the packages listed within it, along with their dependencies.

After successful installation, you should have all the required packages available for your Discord bot. You can then proceed with running your bot.

### Run the bot:
First activate the virtual environment:
 ```shell
 source env/bin/activate
 ```

 Then start the bot with the following:
  ```shell
  python3 bot.py
  ```

- Your bot should now be running and ready to connect to Discord.

### Inviting the bot to the server
To invite your bot to a server, go back to the Discord Developer Portal:
- Select your application and go to the "OAuth2" section in the left sidebar.
- In the "Scopes" section, select the "bot" checkbox.
- In the "Bot Permissions" section, choose the necessary permissions your bot requires. These permissions determine what actions your bot can perform in a server.
- Once you have selected the desired permissions, a URL will be generated under the "Scopes" section.
- Copy the generated URL and open it in a web browser.
- Select the server where you want to invite your bot and click "Authorize."
- Complete any additional steps or permissions requested by Discord.
- If everything goes well, your bot should be added to the selected server and ready to use.

## Training the Keras Layer

### Data Collection
Out of the box, the bot may make mistakes or misunderstand certain prompts. However, you can help improve its accuracy by providing feedback on its responses. When the bot misinterprets your request or gives an incorrect response, you can let it know by running the command `/label_last <label>`, where `<label>` represents the appropriate category for the prompt.

<img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Screenshot%202023-08-04%207.46.28%20AM.png?raw=True" alt="Image Description">

* If you were asking the bot to play music, use `/label_last youtube`.
* If you were asking the bot to set a reminder, use `/label_last reminder`.
* If you were requesting a financial chart, use `/label_last interpreter`.
* For any other cases, use `/label_last other`.
  
### Retraining
Once you have collected prompts you wish to include in training the keras layer, an administrator can run `/retrain_keras` to retrain the layer. This process will utilize the labeled data to fine-tune the model and enhance its performance. After retraining, the bot should have an improved understanding of the labeled categories and provide more accurate responses.

By incorporating this training and retraining workflow, you can actively contribute to refining the bot's capabilities and ensuring a better user experience over time.

Plans to replace this layer with a small local pretrained language model are in the works. We need a local layer for relaying tasks, as depending on an API may slow down the bot as we must wait for a response. This is why the bot was designed to use openAi's API only once when using `!fefe`.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please email [support@alshival.com](mailto:support@alshival.com?subject=openAI%20Discord%20Bot), open an issue, or submit a pull request.

# License

[Creative Commons Zero v1.0 Universal](LICENSE)
