sample_data = {
# This first example is code. The purpose is to push `max_sequence_length` to 2000, which is the standard character limit for Discord.
# For longer text, Fefe will ask you to retrain to increase `max_sequence_length`.
    """
    ```
    import discord
    from discord.ext import commands,tasks
    
    from app.config import *
    
    
    # Set up the bot with '!' as the command prefix. 
    # It is set to listen and respond to all types of intents in the server. 
    # You can change the command prefix by replacing '!' with your preferred symbol.
    bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
    
    ########################################################################
    # Bot Boot Sequence
    ########################################################################
    from app.bot_functions import *
    from app.keras_layer import *
    
    # Create the prompts table if needed when the bot starts up
    asyncio.get_event_loop().run_until_complete(create_prompts_table())
    # Create the labeled_prompts table if needed when the bot starts up
    asyncio.get_event_loop().run_until_complete(create_labeled_prompts_table())
    # Create the reminders table if needed when the bot starts up
    asyncio.get_event_loop().run_until_complete(create_reminder_table())
    # train the keras layer
    asyncio.get_event_loop().run_until_complete(train_keras())
    
    ########################################################################
    # Bot Commands
    ########################################################################
    from app.fefe import *
    
    @bot.command()
    async def fefe(ctx,*,message):
        await talk_to_fefe(ctx,message,bot)
    # Used to label the last prompt you sent. 
    @bot.command()
    async def label_last(ctx,label):
        await label_last_prompt(ctx,label)
    
    # '!clear_reminders` command 
    @bot.command()
    async def clear_reminders(ctx):
        await clear_user_reminders(ctx)
    
    # '!retrain_keras' command to retrain the model. Must be run by an administrator.
    @bot.command()
    async def retrain_keras(ctx):
        if ctx.message.author.guild_permissions.administrator:
            await ctx.send('Training. Standby...')
            await train_keras()
            await ctx.send('Training complete.')
        else:
            await ctx.send('Please contact a server admin to update the keras layer')
    # Thi
    ```
    """: 'other',
}
############################################
# Sample Training Data for Reminders
############################################ 
sample_reminders = {
    "Hey, don't forget to pick up the cake for Sarah's birthday tomorrow at 3 PM.",
    "I have a doctor's appointment next Monday at 10 AM. Could you remind me to take my medication before that?",
    "Remind me to water the plants every evening at 6 PM, they need extra care during this hot weather!",
    "Hey, can you remind me to submit the project report by Friday midnight?",
    "I need to mail the gift to Tom before his graduation ceremony at 2 PM. Please set a reminder for that.",
    "Don't forget to turn off the oven after 30 minutes. Set a reminder, so we don't burn the dinner!",
    "Remind me to call Grandma this Sunday at 4 PM, it's been a while since we last talked.",
    "I have an important meeting at work tomorrow at 11 AM. Can you remind me to prepare the presentation?",
    "Please set a reminder for 8 AM to buy the concert tickets before they sell out.",
    "Hey, remind me to take the cookies out of the oven in 15 minutes. I don't want them to get too crispy!",
    "I need to drop off the dry cleaning by 5:30 PM today. Set a reminder so I don't forget, please.",
    "Remind me to check the mailbox at 3 PM. The package I've been waiting for should arrive today.",
    "I have a dental appointment next Wednesday at 2:45 PM. Please remind me to leave work early that day.",
    "Hey, can you remind me to turn on the sprinklers for the garden at 7 AM tomorrow?",
    "Remind me to send out the party invitations two weeks before the big day.",
    "Don't forget to set a reminder to call the insurance company at 9 AM to update our policy.",
    "I need to submit the college application by next Friday at 11:59 PM. Please set a reminder for that.",
    "Hey, remind me to download the new software update for my phone tonight at 9 PM.",
    "Remind me to take the clothes out of the washing machine in an hour. I don't want them to get wrinkled.",
    "I'm planning to start a new book at 8 PM tonight. Please set a reminder for me to relax and read.",
    "Don't forget to buy tickets for the concert on Saturday at 10 AM when they go on sale.",
    "Remind me to call the plumber tomorrow at 1 PM to fix the leaky faucet.",
    "Hey, can you remind me to back up all my important files and documents on the external hard drive at 5 PM?",
    "I need to submit the tax forms by the end of the month. Set a reminder for the deadline, please.",
    "Remind me to pick up the kids from school at 3:30 PM today.",
    "Don't forget to set a reminder for the conference call with the client at 2 PM tomorrow.",
    "I have a reservation at the restaurant for dinner at 7:45 PM. Please remind me to leave on time.",
    "Hey, can you remind me to take my daily vitamins every morning at 8 AM?",
    "Remind me to submit the expense report by Thursday noon, so I get reimbursed on time.",
    "Don't forget to set a reminder for the online yoga class at 6:30 AM. It's a great way to start the day!",
    "Remind me to water the plants at 6 PM, they need extra care during this hot weather!",
    "Remind me to pick up the kids in 45 minutes",
    "Remind me to turn in my homework at midnight",
    "Remind me to call my friend in an hour",
    "Remind me to take the dog for a walk at 6pm",
    "Remind me to pay the bills by the end of the day",
    "Remind me to buy groceries tomorrow",
    "Remind me to water the plants in the morning",
    "Remind me to check my email in 30 minutes",
    "Remind me to pick up my sister from the airport on Friday",
    "Remind me to take out the trash tonight",
    "Remind me to water the plants every Sunday",
    "Remind me to submit the assignment by tomorrow",
    "Remind me to call the insurance company tomorrow",
    "Remind me to do laundry this evening",
    "Remind me to submit the project by the end of the week",
    "Remind me to water the plants every Tuesday",
    "Remind me to pay the bills on the 15th",
    "Remind me to buy a gift for my friend's birthday",
    "Remind me to pick up the kids from school at 3pm",
    "Remind me to schedule a dentist appointment next week",
    "Remind me to buy a gift for my anniversary",
    "Remind me to take my medication at 8am",
    "Remind me to call the client tomorrow morning",
    "Remind me to water the plants every Monday and Thursday",
    "Remind me to pay the electricity bill by Friday",
    "Remind me to feed the dog before leaving the house",
    "Remind me to attend the team meeting on Wednesday",
    "Remind me to check my email in the afternoon",
    "Remind me to return the borrowed books to the library",
    "Remind me to call my parents on their anniversary",
    "Remind me to study for the exam tomorrow",
    "Remind me to water the plants every Wednesday",
    "Remind me to take out the trash every Tuesday and Friday",
    "Remind me to schedule a meeting with the project manager",
    "Remind me to submit the application before the closing time",
    "Remind me to do the laundry on Saturday",
    "Remind me to submit the assignment before the end of the day",
    "Remind me to water the plants every Thursday",
    "Remind me to submit the report by the end of the month",
    "Remind me to call the doctor for an appointment",
    "Remind me to take a break every two hours",
    "Remind me to buy tickets for the concert on Saturday",
    "Remind me to water the plants every Wednesday",
    "Remind me to take out the trash every Tuesday and Friday",
    "Remind me to schedule a meeting with the project manager",
    "Remind me to submit the application before the closing time",
    "Remind me to do the laundry on Saturday",
    "Remind me to submit the assignment before the end of the day",
    "Remind me to water the plants every Thursday",
    "Remind me to submit the report by the end of the month",
    "Remind me to call the doctor for an appointment",
    "Remind me to take a break every two hours",
    "Remind me to buy tickets for the concert on Saturday",
    "Remind me to water the plants every Wednesday",
    "Remind me to take out the trash every Tuesday and Friday",
    "Remind me to schedule a meeting with the project manager",
    "Remind me to submit the application before the closing time",
    "Remind me to do the laundry on Saturday",
    "Remind me to submit the assignment before the end of the day",
    "Remind me to water the plants every Thursday",
    "Remind me to submit the report by the end of the month",
    "Remind me to call the doctor for an appointment",
    "Remind me to take a break every two hours",
    "Remind me to buy tickets for the concert on Saturday",
    "Remind me to water the plants every Wednesday",
    "Remind me to take out the trash every Tuesday and Friday",
    "Remind me to schedule a meeting with the project manager",
    "Remind me to submit the application before the closing time",
    "Remind me to do the laundry on Saturday",
    "Remind me to submit the assignment before the end of the day",
}

reminder_dict = {reminder: 'reminder' for reminder in sample_reminders}

sample_data = {**sample_data,**reminder_dict}

############################################
# Sample training data for youtube requests
############################################ 
youtube = {
    'Play 1999 by Charli XCX',
    'Search YouTube for the latest news',
    'Play Bohemian Rhapsody by Queen',
    'Find a tutorial on how to knit a scarf on YouTube',
    'Play Sweet Child o\' Mine by Guns N\' Roses',
    'Search YouTube for funny cat videos',
    'Play Shape of You by Ed Sheeran',
    'Find a video explaining how to make a paper airplane on YouTube',
    'Play Hotel California by Eagles',
    'Search YouTube for the trailer of the new Avengers movie',
    'Play Thriller by Michael Jackson',
    'Find a video about the benefits of meditation on YouTube',
    'Play Billie Jean by Michael Jackson',
    'Search YouTube for a documentary on space exploration',
    'Play Smells Like Teen Spirit by Nirvana',
    'Find a video tutorial on how to do makeup on YouTube',
    'Play Imagine by John Lennon',
    'Search YouTube for a workout routine for beginners',
    'Play Stairway to Heaven by Led Zeppelin',
    'Find a video about the history of Ancient Egypt on YouTube',
    'Play Uptown Funk by Mark Ronson ft. Bruno Mars',
    'Search YouTube for a travel vlog about Paris',
    'Play Hey Jude by The Beatles',
    'Find a video tutorial on how to cook a vegan lasagna on YouTube',
    'Play Smokey Robinson - Tracks Of My Tears',
    'Search YouTube for a documentary on climate change',
    'Play Thrift Shop by Macklemore & Ryan Lewis',
    'Find a video tutorial on how to style short hair on YouTube',
    'Play Hallelujah by Leonard Cohen',
    'Search YouTube for highlights of the FIFA World Cup',
    'Play Wonderwall by Oasis',
    'Find a video about the history of Ancient Greece on YouTube',
    'Play Dance Monkey by Tones and I',
    'Find a video tutorial on how to make sushi on YouTube',
    'Play Thunderstruck by AC/DC',
    'Search YouTube for cute baby animal videos',
    'Play Bad Guy by Billie Eilish'
}

youtube_dict = {prompt: 'youtube' for prompt in youtube}

sample_data = {**sample_data,**youtube_dict}
    
############################################
# Sample training data for other requests
############################################ 
openAi = {
    "Hey you":'other',
    "Hey.":'other',
    "Hey, what's up.":'other',
    "Hi, how are you":'other',
    "Good morning!":'other',
    "Thank you!":'other',
    "Thanks.":'other',
    "What's the capital of France?": 'other',
    "How do you make a chocolate cake?": 'other',
    "What time does the museum open?": 'other',
    "Who is the author of the Harry Potter series?": 'other',
    "Can you recommend a good restaurant in this area?": 'other',
    "What's the latest news on the stock market?": 'other',
    "Where can I find information about local events?": 'other',
    "How do I reset my password?": 'other',
    "Is there a post office nearby?": 'other',
    "What's the best way to learn a new language?": 'other',
    "Where can I find the nearest gas station?": 'other',
    "Can you recommend a good movie to watch?": 'other',
    "What's the current exchange rate for USD to EUR?": 'other',
    "Where can I buy tickets for a concert?": 'other',
    "Can you give me directions to the nearest hospital?": 'other',
    "Is there a good book club in this area?": 'other',
    "Where can I find a reliable plumber?": 'other',
    "Can you suggest some fun activities to do on the weekend?": 'other',
    "What's the best way to get rid of stains on clothes?": 'other',
    "Where can I find the best coffee in town?": 'other',
    "Can you recommend a good hiking trail nearby?": 'other',
    "What's the average temperature in this city during summer?": 'other',
    "Where can I find the nearest ATM?": 'other',
    "Can you tell me more about the history of this place?": 'other',
    "What's the best way to take care of indoor plants?": 'other',
    "Where can I find information about local public transportation?": 'other',
    "Can you recommend a good website for learning programming?": 'other',
    "What's the best way to stay motivated while studying?": 'other',
    "Where can I find a reliable mechanic for my car?": 'other',
    "Can you suggest some interesting podcasts to listen to?": 'other',
    "What's the best way to save money on groceries?": 'other',
    "Where can I find a good yoga studio in this area?": 'other',
    "Can you recommend a good place to go for a weekend getaway?": 'other',
    "What's the best way to protect my computer from viruses?": 'other',
    "Where can I find information about local tourist attractions?": 'other',
    "Can you suggest some tips for improving productivity at work?": 'other',
    "What's the best way to train for a marathon?": 'other',
    "Where can I find the best pizza in town?": 'other',
    "Can you recommend a good online course for learning photography?": 'other',
    "What's the best way to organize a closet?": 'other',
    "Where can I find the nearest pharmacy?": 'other',
    "Can you suggest some good TED Talks to watch?": 'other',
    "What's the best way to manage stress?": 'other',
    "Where can I find information about local art galleries?": 'other',
    "Can you recommend a good workout routine for beginners?": 'other',
    "When did the battle of the Alamo happen?": 'other',
    "When was the Declaration of Independence signed?": 'other',
    "When did World War II end?": 'other',
    "When was the first moon landing?": 'other',
    "When is the next full moon?": 'other',
    "When did the Battle of Waterloo take place?": 'other',
    "When was the signing of the Magna Carta?": 'other',
    "When did the French Revolution begin?": 'other',
    "When was the fall of the Berlin Wall?": 'other',
    "When did the American Civil War start?": 'other',
    "When was the Renaissance period?": 'other',
    "When was the construction of the Great Wall of China completed?": 'other',
    "When did the Black Death pandemic occur?": 'other',
    "When was the Boston Tea Party?": 'other',
    "When did the Industrial Revolution begin?": 'other',
    "When did the Civil Rights Movement occur?": 'other',
    "Where can I find information about local farmers' markets?": 'other',
    "Can you suggest some healthy recipes for dinner?": 'other',
    "What's the best way to improve my public speaking skills?": 'other',
    "Where can I find the nearest recycling center?": 'other',

############################################
# Sample Code Questions
############################################  
    """
    What's wrong with my code?
    
    ```
    def calculate_average(numbers):
    total = 0
    for num in numbers:
    total += num
    average = total / len(numbers)
    return average
    
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    print(result)
    ```
    """:'other',
    """
    How can I optimize this code?
    ```
    def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
    if nums[i] in nums[i+1:]:
    duplicates.append(nums[i])
    return duplicates
    
    numbers = [1, 2, 3, 4, 5, 3, 6, 7, 8, 4, 9]
    duplicates = find_duplicates(numbers)
    print(duplicates)
    ```
    """:'other',
    """
    How can I sort a list in Python in descending order?
    ```
    numbers = [5, 2, 8, 1, 6]
    sorted_numbers = sorted(numbers, reverse=True)
    print(sorted_numbers)
    ```
    """: 'other',
    """
    What's the syntax for a for loop in JavaScript?
    ```
    for (let i = 0; i < 5; i++) {
        console.log(i);
    }
    ```
    """: 'other',
}

openAi_dict = {prompt:'other' for prompt in openAi}

sample_data = {**sample_data,**openAi_dict}