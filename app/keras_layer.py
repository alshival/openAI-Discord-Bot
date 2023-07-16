from app.config import *

max_sequence_length = None
word_to_index = None
model = None
label_to_index = None 

async def train_keras():
    global max_sequence_length
    global word_to_index
    global label_to_index
    global model
    ############################################
    # Training Data
    ############################################
    
    # When adding new features that require task assignment in the Keras model,
    # make sure to update the list of labels accordingly in conjunction with the changes made in app/keras_layer.py.
    
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
    # Sample Training Data for Reminders
        'Remind me to pick up the kids in 45 minutes': 'reminder',
        'Remind me to turn in my homework at midnight': 'reminder',
        'When is my project due?': 'reminder',
        'Remind me to call my friend in an hour': 'reminder',
        'When is the deadline for my job application?': 'reminder',
        'Remind me to take the dog for a walk at 6pm': 'reminder',
        'When is my meeting with the client?': 'reminder',
        'Remind me to pay the bills by the end of the day': 'reminder',
        'When do I need to submit the report?': 'reminder',
        'Remind me to buy groceries tomorrow': 'reminder',
        'When is my doctor\'s appointment?': 'reminder',
        'Remind me to water the plants in the morning': 'reminder',
        'When is the parent-teacher meeting?': 'reminder',
        'Remind me to check my email in 30 minutes': 'reminder',
        'When do I have to return my library books?': 'reminder',
        'Remind me to pick up my sister from the airport on Friday': 'reminder',
        'what are my reminders?':'reminder',
        'When is the deadline for my project proposal?': 'reminder',
        'Remind me to take out the trash tonight': 'reminder',
        'When do I have to RSVP for the party?': 'reminder',
        'Remind me to water the plants every Sunday': 'reminder',
        'Remind me to submit the assignment by tomorrow': 'reminder',
        'When is the due date for the rent payment?': 'reminder',
        'Remind me to call the insurance company tomorrow': 'reminder',
        'When do I have to pick up the package from the post office?': 'reminder',
        'Remind me to do laundry this evening': 'reminder',
        'When is my training session?': 'reminder',
        'Remind me to submit the project by the end of the week': 'reminder',
        'When do I need to submit the reimbursement form?': 'reminder',
        'Remind me to water the plants every Tuesday': 'reminder',
        'Remind me to pay the bills on the 15th': 'reminder',
        'When is the due date for my tax filing?': 'reminder',
        'Remind me to buy a gift for my friend\'s birthday': 'reminder',
        'Remind me to pick up the kids from school at 3pm': 'reminder',
        'When is the deadline for my project?': 'reminder',
        'Remind me to schedule a dentist appointment next week': 'reminder',
        'When do I need to submit the expense report?': 'reminder',
        'Remind me to buy a gift for my anniversary': 'reminder',
        'When is my meeting with the project team?': 'reminder',
        'Remind me to take my medication at 8am': 'reminder',
        'When is the due date for my rent payment?': 'reminder',
        'Remind me to call the client tomorrow morning': 'reminder',
        'When do I have to pick up the dry cleaning?': 'reminder',
        'Remind me to water the plants every Monday and Thursday': 'reminder',
        'When is the parent-teacher conference?': 'reminder',
        'Remind me to pay the electricity bill by Friday': 'reminder',
        'When do I need to submit the final report?': 'reminder',
        'Remind me to feed the dog before leaving the house': 'reminder',
        'When is the deadline for my scholarship application?': 'reminder',
        'Remind me to attend the team meeting on Wednesday': 'reminder',
        'When do I have to pick up the package from the courier?': 'reminder',
        'Remind me to check my email in the afternoon': 'reminder',
        'When is my doctor\'s appointment for my annual check-up?': 'reminder',
        'Remind me to return the borrowed books to the library': 'reminder',
        'When do I need to submit the project proposal?': 'reminder',
        'Remind me to call my parents on their anniversary': 'reminder',
        'When is the due date for my credit card payment?': 'reminder',
        'Remind me to study for the exam tomorrow': 'reminder',
        'When do I have to pick up the tickets for the concert?': 'reminder',
        'Remind me to water the plants every Wednesday': 'reminder',
        'Remind me to take out the trash every Tuesday and Friday': 'reminder',
        'When do I need to submit the monthly sales report?': 'reminder',
        'Remind me to schedule a meeting with the project manager': 'reminder',
        'Remind me to submit the application before the closing time': 'reminder',
        'When do I have to pick up my passport from the embassy?': 'reminder',
        'Remind me to do the laundry on Saturday': 'reminder',
        'Remind me to submit the assignment before the end of the day': 'reminder',
        'When do I need to pick up the rental car for my trip?': 'reminder',
    # Sample training data for youtube requests
        'Play 1999 by Charli XCX': 'youtube',
        'Search YouTube for the latest news': 'youtube',
        'Play Bohemian Rhapsody by Queen': 'youtube',
        'Find a tutorial on how to knit a scarf on YouTube': 'youtube',
        'Play Sweet Child o\' Mine by Guns N\' Roses': 'youtube',
        'Search YouTube for funny cat videos': 'youtube',
        'Play Shape of You by Ed Sheeran': 'youtube',
        'Find a video explaining how to make a paper airplane on YouTube': 'youtube',
        'Play Hotel California by Eagles': 'youtube',
        'Search YouTube for the trailer of the new Avengers movie': 'youtube',
        'Play Thriller by Michael Jackson': 'youtube',
        'Find a video about the benefits of meditation on YouTube': 'youtube',
        'Play Billie Jean by Michael Jackson': 'youtube',
        'Search YouTube for a documentary on space exploration': 'youtube',
        'Play Smells Like Teen Spirit by Nirvana': 'youtube',
        'Find a video tutorial on how to do makeup on YouTube': 'youtube',
        'Play Imagine by John Lennon': 'youtube',
        'Search YouTube for a workout routine for beginners': 'youtube',
        'Play Stairway to Heaven by Led Zeppelin': 'youtube',
        'Find a video about the history of Ancient Egypt on YouTube': 'youtube',
        'Play Uptown Funk by Mark Ronson ft. Bruno Mars': 'youtube',
        'Search YouTube for a travel vlog about Paris': 'youtube',
        'Play Hey Jude by The Beatles': 'youtube',
        'Find a video tutorial on how to cook a vegan lasagna on YouTube': 'youtube',
        'Play Smokey Robinson - Tracks Of My Tears': 'youtube',
        'Search YouTube for a documentary on climate change': 'youtube',
        'Play Thrift Shop by Macklemore & Ryan Lewis': 'youtube',
        'Find a video tutorial on how to style short hair on YouTube': 'youtube',
        'Play Hallelujah by Leonard Cohen': 'youtube',
        'Search YouTube for highlights of the FIFA World Cup': 'youtube',
        'Play Wonderwall by Oasis': 'youtube',
        'Find a video about the history of Ancient Greece on YouTube': 'youtube',
    # Sample training data for other requests
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
    }

    messages = list(sample_data.keys())
    labels = list(sample_data.values())
    
    ############################################
    # Import labeled prompts
    ############################################
    #---------------------------------------------
    # Check if `data.db` has labeled_prompts table
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    # Execute the query to retrieve the table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    tables = [table[0] for table in tables]
    if 'labeled_prompts' in tables:
        cursor.execute("select prompt,label from labeled_prompts")
        rows = cursor.fetchall()
        if rows is not None:
            dict_rows = [dict(row) for row in rows]
            messages += [row['prompt'] for row in dict_rows]
            labels += [row['label'] for row in dict_rows]
        
    conn.close()
    
    ############################################
    #  Preprocessing
    ############################################
    vocab = set(' '.join(messages).lower().split())
    vocab_size = len(vocab)
    word_to_index = {word: index for index, word in enumerate(vocab)}
    max_sequence_length = max(len(message.split()) for message in messages)
    #---------------------------------------------
    # Convert sentences to numerical sequences
    X = np.zeros((len(messages), max_sequence_length))
    for i, message in enumerate(messages):
        words = message.lower().split()
        for j, word in enumerate(words):
            X[i, j] = word_to_index[word]
      #---------------------------------------------
    # Convert labels to numerical values
    label_to_index = dict(zip(keras_labels,range(len(keras_labels))))#{'reminder': 0, 'other': 1, 'youtube': 2}
    y = np.array([label_to_index[label] for label in labels])

    # Define the model
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=50, input_length=max_sequence_length))
    model.add(GlobalMaxPooling1D())
    model.add(Dense(16, activation='relu'))
    model.add(Dense(len(keras_labels), activation='softmax'))  # assuming you have 3 classes

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) 


    # Train the model
    model.fit(X, y, epochs=epochs, batch_size=1, verbose=1)

############################################
#  Classification Function
############################################
async def classify_prompt(input_string):
    global max_sequence_length
    global word_to_index
    global model

    # Preprocess the input string
    new_sequence = np.zeros((1, max_sequence_length))
    words = input_string.lower().split()
    for j, word in enumerate(words):
        if word in word_to_index:
            new_sequence[0, j] = word_to_index[word]

    # Make prediction
    prediction = model.predict(new_sequence)
    predicted_index = np.argmax(prediction)  # Change here, get the index of max value
    index_to_label = {v: k for k, v in label_to_index.items()}
    predicted_label = index_to_label[predicted_index]

    return predicted_label

