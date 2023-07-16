
#  openAI Discord Bot 
### [Alshival's Data Service](https://alshival.com)
Demo: [Vimeo](https://vimeo.com/845117509)

This Discord bot utilizes OpenAI's GPT models and provides additional functionalities like setting reminders and playing music with the help of a sqlite database, a keras layer, and Google's Youtube. Created by [Alshival's Data Service](https://alshival.com) to enhance your Discord server experience. For personal use, a group of friends, a study group, or for project management. 

Study groups can benefit from a Discord bot that utilizes OpenAI's GPT models. It can provide instant answers to questions, assist with research, and facilitate discussions on various topics. Discord bots integrated with OpenAI's GPT models can enhance collaboration within teams and projects. They can help generate ideas, provide suggestions, and assist with brainstorming sessions.

<img src="https://github.com/alshival/openAI-Discord-Bot/blob/main/app/Screenshot%202023-07-14%205.20.08%20PM.png?raw=True" alt="Image Description">

Discord servers dedicated to programming, technology, or data science can leverage an OpenAI-powered bot for code assistance, troubleshooting, and answering technical queries. Discord servers centered around creative writing, storytelling, or roleplaying can use a bot with OpenAI's GPT models to generate prompts, develop characters, and facilitate interactive storytelling experiences. Gaming communities can incorporate an OpenAI-powered bot into their Discord server to provide in-game tips, strategies, and assist with game-related queries.

## Features

- Chat with the bot using OpenAI's GPT models
- Ask the bot to set reminders for you.
- Ask the bot to play music through voice channels

## Usage

- Use the command prefix `!` to interact with the bot.
- Example commands:
  - `!fefe <message>`: Chat with the bot using OpenAI's GPT models.
  - `!label_last <label>`: Label the last prompt you sent.
  - `!clear_reminders`: Clear all reminders set by the user.
  - `!retrain_keras`: Retrain the Keras layer. (Only accessible to server administrators)

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
We suggest installing the bot's python dependencies in a virtual environment. 
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
Out of the box, the bot may make mistakes or misunderstand certain prompts. However, you can help improve its accuracy by providing feedback on its responses. When the bot misinterprets your request or gives an incorrect response, you can let it know by running the command `!label_last <label>`, where `<label>` represents the appropriate category for the prompt.

If you were asking the bot to play music, use `!label_last youtube`.
If you were asking the bot to set a reminder, use `!label_last reminder`.
For any other cases, use `!label_last other`.

### Retraining

Once you have labeled a series of prompts, a Discord server administrator can initiate the retraining of the Keras layer from within Discord by running the command `!retrain_keras`. This process will utilize the labeled data to fine-tune the model and enhance its performance. After retraining, the bot should have an improved understanding of the labeled categories and provide more accurate responses.

By incorporating this training and retraining workflow, you can actively contribute to refining the bot's capabilities and ensuring a better user experience over time.
## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please email [support@alshival.com](mailto:support@alshival.com?subject=openAI%20Discord%20Bot), open an issue, or submit a pull request.

# License

[Creative Commons Zero v1.0 Universal](LICENSE)
