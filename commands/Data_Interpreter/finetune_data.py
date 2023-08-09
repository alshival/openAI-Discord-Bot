finetune = [
{'role':'user','content':"""

filename:
```
app/downloads/sample_database_2.csv
```

columns:
```
Age              int64
Home State      object
Education       object
Eye Color       object
Attribute 1      int64
Attribute 2      int64
Attribute 3      int64
Attribute 4      int64
Attribute 5      int64
Attribute 6      int64
Attribute 7      int64
Attribute 8      int64
Attribute 9      int64
Attribute 10     int64
dtype: object
```

First 3 rows:
```
   Age   Home State    Education Eye Color  Attribute 1  Attribute 2  Attribute 3  Attribute 4  Attribute 5  Attribute 6  Attribute 7  Attribute 8  Attribute 9  Attribute 10
0   56     Delaware  High School      Blue            0            0            1            1            1            1            0            0            0             0
1   46  Mississippi          PhD     Hazel            1            1            0            0            0            1            0            0            1             0
2   32       Hawaii  High School     Hazel            0            0            1            0            1            1            1            0            0             1
```

request:
```
create a state choropleth leaflet containing the number of people who reside in each state.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import geopandas as gpd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/us-states.json')

# Group by state and count the number of people
state_data = data.groupby('Home State').size().reset_index(name='Count')

# Merge data with gdf on state column
merged_data = gdf.merge(state_data, left_on='name', right_on='Home State')

# Create a choropleth map to show the count in each state
m = folium.Map(location=[37, -102], zoom_start=4)

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['Home State', 'Count'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of People'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/state_choropleth.html"
# Save the map as an HTML file
m.save(filename)
"""},
{'role':'user','content':"""

filename:
```
app/downloads/iris_dataset.csv
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

First 3 rows:
```
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
```

request:
```
Create a pair plot using this data.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Assuming your data is in a DataFrame called `data`
# Load the iris dataset
data = pd.read_csv('app/downloads/iris_dataset.csv')

# Create a pair plot
sns.pairplot(data, hue='species')

# Set variable filename (required)
filename = "app/downloads/pair_plot.png"
# Save the pair plot as an image file
plt.savefig(filename)

"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
Who are the youngest passengers who died?
```

"""},
{'role':'assistant','content':"""
import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Filter the dataset to get the youngest passengers who died
youngest_passengers_died = data[data['survived'] == 0].sort_values('age').head()

# Print the results
print(youngest_passengers_died.to_string())
"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
Who are the oldest passengers who died?
```

"""},
{'role':'assistant','content':"""
import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Filter the dataset to get the youngest passengers who died
youngest_passengers_died = data[data['survived'] == 0].sort_values('age', ascending=False).head()

# Print the results
print(youngest_passengers_died.to_string())

"""},
{'role':'user','content':"""

filename:
```
app/downloads/sample_database_2.csv
```

columns:
```
Age              int64
Home State      object
Education       object
Eye Color       object
Attribute 1      int64
Attribute 2      int64
Attribute 3      int64
Attribute 4      int64
Attribute 5      int64
Attribute 6      int64
Attribute 7      int64
Attribute 8      int64
Attribute 9      int64
Attribute 10     int64
dtype: object
```

First 3 rows:
```
   Age   Home State    Education Eye Color  Attribute 1  Attribute 2  Attribute 3  Attribute 4  Attribute 5  Attribute 6  Attribute 7  Attribute 8  Attribute 9  Attribute 10
0   56     Delaware  High School      Blue            0            0            1            1            1            1            0            0            0             0
1   46  Mississippi          PhD     Hazel            1            1            0            0            0            1            0            0            1             0
2   32       Hawaii  High School     Hazel            0            0            1            0            1            1            1            0            0             1
```

request:
```
Who has blue eyes?
```

"""},
{'role':'assistant','content':"""

import pandas as pd

# Assuming your data is in a DataFrame called `data`
# Load the sample database
data = pd.read_csv('app/downloads/sample_database_2.csv')

# Filter the dataset to get the people with blue eyes
people_with_blue_eyes = data[data['Eye Color'] == 'Blue']

# Print the results
print(people_with_blue_eyes.to_string())
"""},
{'role':'user','content':"""

filename:
```
app/downloads/titanic_dataset.csv
```

columns:
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
dtype: object
```

First 3 rows:
```
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
```

request:
```
create a plotly histogram for age of survivors and dead.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import plotly.express as px

# Assuming your data is in a DataFrame called `data`
# Load the Titanic dataset
data = pd.read_csv('app/downloads/titanic_dataset.csv')

# Set the dark theme using plotly
px.defaults.template = "plotly_dark"

# Create a histogram for age of survivors and dead
fig = px.histogram(data, x="age", color="survived", nbins=30)

# Save the figure
# Set save filename
save_filename = "app/downloads/titanic_plotly.html"
fig.write_html(save_filename)

# Show the plot
fig.show()
"""},
{'role':'user','content':"""

filename:
```
app/downloads/sample_database_2.csv
```

columns:
```
Age              int64
Home State      object
Education       object
Eye Color       object
Attribute 1      int64
Attribute 2      int64
Attribute 3      int64
Attribute 4      int64
Attribute 5      int64
Attribute 6      int64
Attribute 7      int64
Attribute 8      int64
Attribute 9      int64
Attribute 10     int64
dtype: object
```

request:
```
Create a state choropleth leaflet.
```

"""},
{'role':'assistant','content':"""
import pandas as pd
import geopandas as gpd
import folium

# Assuming your data is in a DataFrame called `data`
# Load the us-states.json file into a GeoDataFrame
gdf = gpd.read_file('app/us-states.json')

# Group by state and count the number of cases
state_data = data.groupby('Home State').size().reset_index(name='Count')

# Merge data with gdf on state column
merged_data = gdf.merge(state_data, left_on='name', right_on='Home State')

# Create a choropleth map to show the count in each state
m = folium.Map(location=[37, -102], zoom_start=4)

folium.Choropleth(
    geo_data=merged_data,
    name='choropleth',
    data=merged_data,
    columns=['Home State', 'Count'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Count'
).add_to(m)

folium.LayerControl().add_to(m)

# Set variable filename (required)
filename = "app/downloads/state_choropleth.html"
# Save the map as an HTML file
m.save(filename)

"""}
]