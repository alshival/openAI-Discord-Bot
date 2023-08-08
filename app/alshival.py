
################################################################
Request: Write a script that spits out an output but will error out.
################################################################

I ran into an Error: 
```
NameError - name 'pd' is not defined
```

Here's the code:

```
filename = "app/downloads/sample_data.csv"

columns = {
    'Person': 'int64',
    'Age': 'int64',
    'Height (cm)': 'int64',
    'Weight (kg)': 'int64',
    'Income ($)': 'int64',
    'Education (years)': 'int64'
}

data = pd.read_csv(filename)

data.columns = columns.keys()
data.dtypes

X = data.drop('Income ($)', axis=1)
y = data['Income ($)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential()
model.add(Dense(10, activation='relu', input_dim=X_train_scaled.shape[1]))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, verbose=0)

loss = model.evaluate(X_test_scaled, y_test)

print("Test Loss:", loss)

# Intentional error to demonstrate exception handling
unknown_variable = some_function()
```
