finetune = [
# Example 1
{'role':'user','content':"""
filename:
```
app/downloads/planets.csv
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
app/downloads/iris.csv
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
app/downloads/titanic.csv
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
app/downloads/modis.csv
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
app/downloads/chicago_crime_data_2.csv
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

"""},

{'role':'user','content':"""

filename:
```
app/downloads/COVID-data-cdc.csv
```

columns:
```
county                                 object
county_fips                             int64
state                                  object
county_population                       int64
health_service_area_number              int64
health_service_area                    object
health_service_area_population        float64
covid_inpatient_bed_utilization       float64
covid_hospital_admissions_per_100k    float64
covid_cases_per_100k                  float64
covid_19_community_level               object
date_updated                           object
dtype: object
```

request:
```
Group the data by state and count the number of cases. Create a map and color each state by the number of cases.
```
"""},
{'role':'assistant','content':"""
import folium
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/us-states.json')

# Group by state and count the number of cases
state_cases = data.groupby('state')['covid_cases_per_100k'].count().reset_index(name='cases_count')

# Merge data with gdf on state column
merged_data = gdf.merge(state_cases, left_on='name', right_on='state')

# Create a choropleth map to show the cases in each state
m = folium.Map(location=[37, -102], zoom_start=4)

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['state', 'cases_count'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='COVID Cases per 100k'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/covid_choropleth.html"
# Save the map as an HTML file
m.save(filename)

"""},
{'role':'user','content':"""

filename:
```
app/downloads/COVID-data-cdc.csv
```

columns:
```
county                                 object
county_fips                             int64
state                                  object
county_population                       int64
health_service_area_number              int64
health_service_area                    object
health_service_area_population        float64
covid_inpatient_bed_utilization       float64
covid_hospital_admissions_per_100k    float64
covid_cases_per_100k                  float64
covid_19_community_level               object
date_updated                           object
dtype: object
```

request:
```
Can you group by state and count the number of cases in each state? Then create a map with states colored in with a purple or blue spectrum. Use a dark tile layer: `TileLayer('cartodbdark_matter')`.
```

"""},
{'role':'assistant','content':"""
import folium
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/us-states.json')

# Group by state and count the number of cases
state_cases = data.groupby('state')['covid_cases_per_100k'].count().reset_index(name='cases_count')

# Merge data with gdf on state column
merged_data = gdf.merge(state_cases, left_on='name', right_on='state')

# Create a choropleth map to show the cases in each state
m = folium.Map(location=[37, -102], zoom_start=4, tiles='cartodbdark_matter')

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['state', 'cases_count'],
    key_on='feature.properties.name',
    fill_color='PuRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='COVID Cases'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/covid_choropleth.html"
# Save the map as an HTML file
m.save(filename)
"""}
]