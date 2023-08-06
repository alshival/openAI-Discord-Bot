finetune = [
# Example 1
{'role':'user','content':"""
filename:
```
planets.csv
```

columns:
```
method             object
number              int64
orbital_period    float64
mass              float64
distance          float64
year                int64
dtype: object
```

request:
```
Plot orbital_period by mass.
```
"""},
{'role':'assistant','content':"""
```python
import matplotlib.pyplot as plt
plt.clf()
# Assuming your data is in a DataFrame called `data`
plt.scatter(data['mass'], data['orbital_period'])
plt.xlabel('Mass')
plt.ylabel('Orbital Period')
plt.title('Orbital Period by Mass')

# Set variable filename (required)
filename = "app/downloads/planets.png"
# save plot
plt.savefig(filename, dpi=300, bbox_inches='tight')
```
"""},
# Example 2
{'role':'user','content':"""
filename:
```
iris.csv
```

columns:
```
sepal_length    float64
sepal_width     float64
petal_length    float64
petal_width     float64
species          object
dtype: object
```

request:
```
Create a pair plot.
```
"""},
{'role':'assistant','content':"""
```python
import seaborn as sns
import matplotlib.pyplot as plt
plt.clf()

# Assuming your data is in a DataFrame called `data`
sns.pairplot(data, hue='species')

# Set variable filename (required)
filename = "app/downloads/iris.png"
# save plot
plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
# Example 3
{'role':'user','content':"""
filename:
```
titanic.csv
```

columns:
```
survived          int64
pclass            int64
sex              object
age             float64
sibsp             int64
parch             int64
fare            float64
embarked         object
class          category
who              object
adult_male         bool
deck           category
embark_town      object
alive            object
alone              bool
dtype: object
```

request:
```
Create a pair plot.
```
"""},
{'role':'assistant','content':"""
import seaborn as sns
plt.clf()

# Assuming your data is in a DataFrame called `data`
sns.pairplot(data)

# Set variable filename (required)
filename = "titanic.png"
# save plot
plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':'''
filename
```
modis.csv
```

columns:
```
latitude      float64
longitude     float64
brightness    float64
scan          float64
track         float64
acq_date       object
acq_time        int64
satellite      object
confidence      int64
version        object
bright_t31    float64
frp           float64
daynight       object
dtype: object
```

request:
```
plot brightness by confidence, and set hue to the satellite type.
```
'''},
{'role':'assistant','content':"""
import seaborn as sns
import matplotlib.pyplot as plt
plt.clf()

# Assuming your data is in a DataFrame called `data`
sns.set(style="darkgrid")
sns.scatterplot(data=data, x='confidence', y='brightness', hue='satellite')

# Set variable filename (required)
filename = "app/downloads/modis.png"
# save plot
plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"""

filename:
```
chicago_crime_data_2.csv
```

columns:
```
date             object
primary_type     object
latitude        float64
longitude       float64
dtype: object
```

request:
```
Plot latitude and longitude on a folium map where primary_type = HOMICIDE. Center the map around the city of Chicago. Use red circle markers for the points.
```

"""},
{'role':'assistant','content':"""
import folium

# Assuming your data is in a DataFrame called `data`
chicago_coordinates = (41.8781, -87.6298)  # Coordinates of Chicago

# Filter data for primary_type = HOMICIDE
homicide_data = data[data['primary_type'] == 'HOMICIDE']

# Create a folium map centered around Chicago
m = folium.Map(location=chicago_coordinates, zoom_start=10)

# Add circle markers for each homicide incident
for index, row in homicide_data.iterrows():
    folium.CircleMarker(location=(row['latitude'], row['longitude']), radius=5, color='red', fill=True, fill_color='red').add_to(m)

# Set variable filename (required)
filename = "app/downloads/chicago_crime_map.html"
# Save the map as an HTML file
m.save(filename)

"""}
]