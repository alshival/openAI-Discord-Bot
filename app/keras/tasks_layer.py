from app.config import *
from app.keras import sample_prompts
model_file = 'app/keras/tasks_layer.keras'
parameters_file = 'app/keras/parameters.pkl'

async def train_tasks_layer():
    global model
    global max_sequence_length
    global word_to_index
    global label_to_index
    global embedding_dim
    ############################################
    # Training Data
    ############################################
    # When adding new features that require task assignment in the Keras model,
    # make sure to update the list of labels accordingly in conjunction with the changes made in app/keras_layer.py.

    messages = list(sample_prompts.sample_data.keys())
    labels = list(sample_prompts.sample_data.values())
    
    ############################################
    # Import labeled prompts
    ############################################
    #---------------------------------------------
    # Check if `data.db` has labeled_prompts table
    conn = await create_connection()
    conn.row_factory = sqlite3.Row
    cursor = await conn.cursor()
    # Execute the query to retrieve the table names
    await cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = await cursor.fetchall()
    tables = [table[0] for table in tables]
    if 'labeled_prompts' in tables:
        await cursor.execute("select prompt,label from labeled_prompts")
        rows = await cursor.fetchall()
        if rows is not None:
            dict_rows = [dict(row) for row in rows]
            messages += [row['prompt'] for row in dict_rows]
            labels += [row['label'] for row in dict_rows]
        
    await conn.close()
    
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

    # Save the model as a HDF5
    model.save(model_file)

    # Save the parameters to the pickle file
    parameters = {
        'max_sequence_length': max_sequence_length,
        'word_to_index': word_to_index,
        'label_to_index': label_to_index,
        #'embedding_dim': embedding_dim,
        
    }
    
    with open(parameters_file, 'wb') as f:
        pickle.dump(parameters, f)

############################################
#  load model
############################################
async def load_tasks_layer():
    global model
    global max_sequence_length
    global word_to_index
    global label_to_index
    global embedding_dim
    
    if os.path.exists(model_file):
        reminder_model = load_model(model_file)
        # Load the parameters from the pickle file
        with open(parameters_file, 'rb') as f:
            parameters = pickle.load(f)
        max_sequence_length = parameters['max_sequence_length']
        word_to_index = parameters['word_to_index']
        label_to_index = parameters['label_to_index']
        #embedding_dim = parameters['embedding_dim']
    else:
        await train_tasks_layer()
        
    # Load the model
    model = load_model(model_file)

############################################
#  Classification Function
############################################
async def classify_prompt(prompt):

    # Preprocess the prompt
    prompt = prompt.lower().split()
    numerical_sequence = [word_to_index[word] for word in prompt if word in word_to_index]

    # Convert the numerical sequence to a numpy array and pad if needed
    numerical_sequence = np.array([numerical_sequence])
    padded_sequence = pad_sequences(numerical_sequence, maxlen=max_sequence_length)

    # Make the prediction
    predictions = model.predict(padded_sequence)
    predicted_label_index = np.argmax(predictions[0])

    # Map the predicted label index back to the original label
    index_to_label = {index: label for label, index in label_to_index.items()}
    predicted_label = index_to_label[predicted_label_index]

    return predicted_label
