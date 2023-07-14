
#  openAI Discord Bot 
### [Alshival's Data Service](https://alshival.com)
Demo: [Vimeo](https://vimeo.com/845117509)

This Discord bot utilizes OpenAI's GPT models and provides additional functionalities like setting reminders and playing music. Created by [Alshival's Data Service](https://alshival.com) to enhance your Discord server experience.

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

## Installation

1. Clone the repository:

   ```shell
   gh repo clone alshival/openAi-Discord-Bot
   ```

2. Install the required dependencies:
     - will complete soon.

4. Set the environmental variables referenced in `app/config.py`:

   - DISCORD_BOT_TOKEN
   - OPENAI_API_KEY
   - google_api_key (Need Youtube Data API enabled for music playback)

5. Run the bot:

   ```shell
   python bot.py
   ```

## Training the Keras Layer

#### Data Collection
Out of the box, the bot may make mistakes or misunderstand certain prompts. However, you can help improve its accuracy by providing feedback on its responses. When the bot misinterprets your request or gives an incorrect response, you can let it know by running the command `!label_last <label>`, where `<label>` represents the appropriate category for the prompt.

If you were asking the bot to play music, use `!label_last youtube`.
If you were asking the bot to set a reminder, use `!label_last reminder`.
For any other cases, use `!label_last other`.

#### Retraining

Once you have labeled a series of prompts, a server administrator can initiate the retraining of the Keras layer by running the command `!retrain_keras`. This process will utilize the labeled data to fine-tune the model and enhance its performance. After retraining, the bot should have an improved understanding of the labeled categories and provide more accurate responses.

By incorporating this training and retraining workflow, you can actively contribute to refining the bot's capabilities and ensuring a better user experience over time.
## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please email [support@alshival.com](mailto:support@alshival.com?subject=openAI%20Discord%20Bot), open an issue, or submit a pull request.

## License

[License](LICENSE)
