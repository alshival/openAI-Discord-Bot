
################################################################
Output:
################################################################

################################################################
Fine-tuning:
################################################################
{'role':'user','content':"""Create a business listing dataset. 100 business with info about type of business, latitude and longitude, and also whether they are open at the current moment or not."""},
{'role':'assistant','content':"""
import pandas as pd
import random

# Generate random latitude and longitude values within a specific range
def generate_coordinates():
    latitude = round(random.uniform(40.0, 41.0), 6)
    longitude = round(random.uniform(-74.0, -73.0), 6)
    return latitude, longitude

# Generate a random boolean value to indicate whether a business is open or not
def generate_open_status():
    return random.choice([True, False])

# Generate a business listing dataset
businesses = []
for _ in range(100):
    business = {
        'Business Name': f'Business {_}',
        'Type of Business': random.choice(['Restaurant', 'Retail', 'Salon', 'Gym', 'Cafe']),
        'Latitude': generate_coordinates()[0],
        'Longitude': generate_coordinates()[1],
        'Open': generate_open_status()
    }
    businesses.append(business)

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(businesses)

# Save the DataFrame as a CSV file
filename = "app/downloads/business_listings.csv"
df.to_csv(filename, index=False)

"""}