from app.config import * 
from app.bot_functions import *

# There are different reminder tasks one could do. Setting a reminder is a different task than looking up a reminder.
# The first keras layer decides that the prompt is a reminder.
# Now, we pass that prompt through a second keras layer to help decide which type of reminder task the user wishes to achieve.

from app.config import *

reminder_model = None
max_sequence_length_reminders = None
word_to_index_reminders = None
label_to_index_reminders = None
# Location to the pretrained model:
model_file = 'app/reminders/keras_reminder_layer_pretrained.keras'
parameters_file = 'app/reminders/reminder_model_parameters.pickle'
############################################
#  Train function
############################################
async def train_reminder_layer():
    print('Training the reminder task layer')
    
    global reminder_model
    global max_sequence_length_reminders
    global word_to_index_reminders
    global label_to_index_reminders
    # These are essentially the tasks our bot can do.
    reminder_keras_labels = ['reminder','reminder-lookup']
    ############################################
    # Training Data
    ############################################ 

    sample_data = {
    # Setting Reminders
        'Remind me to pick up the kids in 45 minutes': 'reminder',
        'Remind me to turn in my homework at midnight': 'reminder',
        'Remind me to call my friend in an hour': 'reminder',
        'Remind me to take the dog for a walk at 6pm': 'reminder',
        'Remind me to pay the bills by the end of the day': 'reminder',
        'Remind me to buy groceries tomorrow': 'reminder',
        'Remind me to water the plants in the morning': 'reminder',
        'Remind me to check my email in 30 minutes': 'reminder',
        'Remind me to pick up my sister from the airport on Friday': 'reminder',
        'Remind me to pick up the kids from school at 3pm': 'reminder',
        'Remind me to turn off the oven in 10 minutes': 'reminder',
        'Remind me to call my dentist next week': 'reminder',
        'Remind me to feed the cat at 7am': 'reminder',
        'Remind me to send the report before the end of the day': 'reminder',
        'Remind me to book a hotel for the vacation': 'reminder',
        'Remind me to take my medication in the evening': 'reminder',
        'Remind me to check my phone in an hour': 'reminder',
        'Remind me to attend the meeting on Monday': 'reminder',
        'Remind me to submit the assignment by Friday': 'reminder',
        'Remind me to water the plants every evening': 'reminder',
        'Remind me to pay the rent by the 5th of next month': 'reminder',
        'Remind me to buy a birthday gift for my friend': 'reminder',
        'Remind me to clean the house on Saturday': 'reminder',
        'Remind me to call my parents tomorrow': 'reminder',
        'Remind me to check the mail in the afternoon': 'reminder',
        'Remind me to pick up the dry cleaning on Wednesday': 'reminder',
        'Remind me to study for the exam next week': 'reminder',
        'Remind me to renew my subscription before it expires': 'reminder',
        'Remind me to set up a meeting with the client': 'reminder',
    # Looking Up Reminders
        'what are my reminders?':'reminder-lookup',
        'What reminders have I set?': 'reminder-lookup',
        'Any reminders?':'reminder-lookup',
        'When is my project due?': 'reminder-lookup',
        'When is the deadline for the job application?': 'reminder-lookup',
        'When is the meeting with the client?': 'reminder-lookup',
        'When do I need to submit the report?': 'reminder-lookup',
        'When is the doctor\'s appointment?': 'reminder-lookup',
        'When is the parent-teacher meeting?': 'reminder-lookup',
        'When do I have to return the library books?': 'reminder-lookup',
        'what are my reminders?':'reminder-lookup',
        'When is my project due?': 'reminder-lookup',
        'When is the deadline for the job application?': 'reminder-lookup',
        'When is the meeting with the client?': 'reminder-lookup',
        'When do I need to submit the report?': 'reminder-lookup',
        'When is the doctor\'s appointment?': 'reminder-lookup',
        'When is the parent-teacher meeting?': 'reminder-lookup',
        'When do I have to return the library books?': 'reminder-lookup',
        'What are my reminders for today?': 'reminder-lookup',
        'What\'s on my schedule for tomorrow?': 'reminder-lookup',
        'Can you tell me when my next appointment is?': 'reminder-lookup',
        'What is the due date for the project proposal?': 'reminder-lookup',
        'When is the deadline for submitting the expense report?': 'reminder-lookup',
        'Can you remind me when I need to pay my bills?': 'reminder-lookup',
        'When is the deadline for the scholarship application?': 'reminder-lookup',
        'When do I have to RSVP for the event?': 'reminder-lookup',
        'What are the important dates on my calendar this month?': 'reminder-lookup',
        'Can you let me know when my subscription renews?': 'reminder-lookup',
        'When do I need to renew my driver\'s license?': 'reminder-lookup',
        'What time is my dentist appointment?': 'reminder-lookup',
        'When is the deadline for the grant application?': 'reminder-lookup',
        'When is my next team meeting?': 'reminder-lookup',
        'Can you remind me when I have to pick up the kids from school?': 'reminder-lookup',
        'When is the due date for the rent payment?': 'reminder-lookup',
        'What time is my flight tomorrow?': 'reminder-lookup',
        'When is the deadline for submitting the manuscript?': 'reminder-lookup',
        'Can you tell me when I have to submit the project?': 'reminder-lookup',
        'What are the tasks on my to-do list for today?': 'reminder-lookup',
        'When is my next performance review?': 'reminder-lookup',
        'When is the deadline for the conference registration?': 'reminder-lookup',
        'Can you remind me when I have to pick up the prescription?': 'reminder-lookup',
        'When do I need to schedule a follow-up appointment?': 'reminder-lookup',
    }
    prompts = list(sample_data.keys())
    labels = list(sample_data.values())

    #  Preprocessing
    vocab = set(' '.join(prompts).lower().split())
    vocab_size = len(vocab)
    word_to_index_reminders = {word: index for index, word in enumerate(vocab)}
    max_sequence_length_reminders = max(len(prompt.split()) for prompt in prompts)

    # Convert sentences to numerical sequences
    X = np.zeros((len(prompts), max_sequence_length_reminders))
    for i, prompt in enumerate(prompts):
        words = prompt.lower().split()
        for j, word in enumerate(words):
            X[i, j] = word_to_index_reminders[word]
            
    # Convert labels to numerical values
    label_to_index_reminders = dict(zip(reminder_keras_labels,range(len(reminder_keras_labels))))
    y = np.array([label_to_index_reminders[label] for label in labels])
    # Define the model
    
    reminder_model = Sequential()
    reminder_model.add(Embedding(input_dim=vocab_size, output_dim=32, input_length=max_sequence_length_reminders))
    reminder_model.add(Flatten())
    reminder_model.add(Dense(8, activation='relu'))
    reminder_model.add(Dense(len(reminder_keras_labels), activation='softmax')) 
    
    # Compile the model
    reminder_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) 

    # Train the model
    reminder_model.fit(X, y, epochs=epochs, batch_size=1, verbose=1)

    # Save the model as a HDF5
    
    reminder_model.save(model_file)

    # Save the parameters to the pickle file
    parameters = {
        'max_sequence_length_reminders': max_sequence_length_reminders,
        'word_to_index_reminders': word_to_index_reminders,
        'label_to_index_reminders': label_to_index_reminders,
    }
    with open(parameters_file, 'wb') as f:
        pickle.dump(parameters, f)
    
    print('Training the reminder task layer complete')

############################################
#  load model
############################################
async def load_reminder_layer():
    global reminder_model
    global max_sequence_length_reminders
    global word_to_index_reminders
    global label_to_index_reminders
    
    if os.path.exists(model_file):
        reminder_model = load_model(model_file)
        # Load the parameters from the pickle file
        with open(parameters_file, 'rb') as f:
            parameters = pickle.load(f)
        max_sequence_length_reminders = parameters['max_sequence_length_reminders']
        word_to_index_reminders = parameters['word_to_index_reminders']
        label_to_index_reminders = parameters['label_to_index_reminders']
    else:
        await train_reminder_layer()
    
############################################
#  Classification Function
############################################
async def classify_reminder(input_string):
    # Preprocess the input string
    input_string = input_string.lower()
    words = input_string.split()
    input_sequence = np.zeros((1, max_sequence_length_reminders))
    for i, word in enumerate(words):
        if word in word_to_index_reminders:
            input_sequence[0, i] = word_to_index_reminders[word]

    # Make predictions
    predicted_index = np.argmax(reminder_model.predict(input_sequence))
    predicted_label = list(label_to_index_reminders.keys())[predicted_index]

    return predicted_label

# Set a reminder
async def set_reminder(ctx,message,model,db_conn):
    messages = []
    messages.extend([{'role':'user','content':'remind me to turn in my homework next week in the morning.'},
                    {'role':'assistant','content':"""{"message":"Turn in homework","reminder_time":"(datetime.now() + timedelta(weeks=1)).strftime('%Y-%m-%d 09:00:00')"} """}])
    messages.extend([{'role': 'user', 'content': "Remind me in three hours to pick up the kids."},
                  {'role': 'assistant', 'content': """{"message":"Pick up the kids","reminder_time":"(datetime.now() + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:00')"} """}])
    messages.extend([{'role': 'user', 'content': 'Remind me to buy groceries tomorrow.'},
                    {'role': 'assistant', 'content': """{"message":"Buy groceries","reminder_time":"(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:00')"} """}])
    messages.extend([{'role': 'user', 'content': 'Remind me in 30 minutes to call my mom.'},
                     {'role': 'assistant', 'content': """{"message":"Call mom","reminder_time":"(datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:00')"} """}])
    messages.append({'role':'user','content':f'Put this in the same format as before: {message}'})
    
    response = openai.ChatCompletion.create(
        model=model,
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
    try:
        response_text = eval(response_text)
    
        reminder_time = eval(response_text['reminder_time'])
    except Exception as e:
        await ctx.send(response_text)
    
    dictionary = {
        'message': response_text['message'],
        'response_time': reminder_time
    }
    
    await store_prompt(db_conn, ctx.author.name, message, model, f"Reminder set for {reminder_time}.", ctx.channel.name,keras_classified_as='reminder')
    
    # Add the new reminder to the database
    await add_reminder(ctx.author.name, response_text['message'], ctx.channel.id, ctx.channel.name, reminder_time)
    await ctx.send(f"Reminder set for {reminder_time}.")

# Look up a reminder
async def reminder_lookup(ctx, message, model, db_conn):
    cursor = await db_conn.cursor()
    await cursor.execute(f"SELECT reminder, reminder_time FROM reminders where username = ?",(ctx.author.name,))
    rows = await cursor.fetchall()

    # Create a markdown table header
    response = "Here are your reminders:\n"
    #table = "| Reminder | Reminder Time  |\n"
    #table += "|----------|---------------|--------------|\n"

    # Add each reminder to the table
    for row in rows:
        reminder = row[0]
        reminder_time = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")

        # Add the reminder details to the table row
        response += f"{reminder} : {reminder_time}\n"

    # Send the table as a message
    await ctx.send(f"```markdown\n{response}```")
    await store_prompt(db_conn, ctx.author.name, message, model, response, ctx.channel.name,keras_classified_as='reminder')

# Final reminder function
async def reminder(ctx,message,model,db_conn):
    try:
        message_category = await classify_reminder(message)
    except Exception as e:
        # Capture the error message
        error_message = str(e)
        print(type(message))
        print(message)
        await ctx.send(f"""
        MMMM.... Sorry... I am a bit confused by that question. Can you flag it for developers?
        """)
        await store_prompt(db_conn, ctx.author.name, message, model,'', ctx.channel.name,keras_classified_as = 'ERROR.REMINDER')
        return

    # bot's Reminder Capabilities
    if message_category == 'reminder':
        await set_reminder(ctx,message,model,db_conn)
    # Bot's openAi capabilities
    elif message_category == 'reminder-lookup':
        await reminder_lookup(ctx,message,model,db_conn)