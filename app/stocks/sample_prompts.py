sample_prompts = [
#######################################################
# Example 1 - Updated Format
#######################################################
    {'role':'user','content':'Can you plot Microsoft\'s stock price for the last four quarters? Add a line of best fit for the last two quarters.'},
    {'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Microsoft
ticker = "MSFT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Microsoft using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Microsoft's brand colors
colors = ['#3C6EB4', '#FFB900', '#B4009E', '#00A300']
sns.set_palette(sns.color_palette(colors))

# Calculate the start date as two quarters (six months) ago
start_date_two_quarters_ago = end_date - timedelta(days=182)

# Filter the historical data for Microsoft for the past two quarters 
data_two_quarters = data[data.index.to_series() > start_date_two_quarters_ago]

# Take our dates as X. Convert datetime to numerical values.
X = pd.DataFrame((data_two_quarters.index - start_date_two_quarters_ago).days)

# Take our close price as Y
y = pd.Series(data_two_quarters["Close"])

# Fit a linear regression model
regressor = LinearRegression()
regressor.fit(X, y)

# Predict the stock prices using the linear regression model
predicted_prices = regressor.predict(X)

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Microsoft for the past two quarters
plt.plot(data.index, data["Close"], label="Microsoft (MSFT)")

# Plot the linear regression line
plt.plot(data_two_quarters.index, predicted_prices, color='red', linestyle='--', label='Linear Regression')

plt.title("Microsoft Stock Price (Last Two Quarters)", fontsize=16, fontweight='bold', color="#333333")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""
    },
#######################################################
# Example 2 - Updated Format
#######################################################
    {'role':'user',
     'content':"How has Bumble and Match Group been doing the past 5 quarters? Can you plot percent change and add a line of best fit for the latest quarter?"},
    {'role':'assistant',
     'content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbols for Bumble and Match Group
tickers = ["BMBL", "MTCH"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Bumble and Match Group using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the "Close" price for Bumble and Match Group for the past two quarters
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.plot(data.index, data[tickers[0]], label="Bumble", color='red')  # Switched to red color
plt.plot(data.index, data[tickers[1]], label="Match Group", color='purple')  # Switched to pink color

plt.title("Bumble and Match Group Stock Prices (Last Two Quarters)", fontsize=16, fontweight='bold', color="#000000")  # Change color to black
plt.xlabel("Date", fontsize=14, color="#333333")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#333333")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""
    },
#######################################################
# Example 3 
#######################################################
     {'role':'user','content':'Hey, can you show percent change for Bitcoin and Ethereum\'s price for the past two quarters?'},
    {'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename  # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbols for Bitcoin and Ethereum
symbols = ["BTC-USD", "ETH-USD"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Bitcoin and Ethereum using yfinance
data = yf.download(symbols, start=start_date, end=end_date)

percent_change = data["Close"].pct_change().dropna()*100
# Set a custom color palette for Bitcoin and Ethereum
colors = ['#FFA500', '#0000FF']  # Orange for Bitcoin, Blue for Ethereum
sns.set_palette(sns.color_palette(colors))


# Set black background theme for the plot using Matplotlib
plt.style.use('dark_background')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the percent change for Bitcoin and Ethereum for the past two quarters. Must drop na.
plt.plot(percent_change.index, percent_change["BTC-USD"], label="Bitcoin (BTC)", color='#FFA500')
plt.plot(percent_change.index, percent_change["ETH-USD"], label="Ethereum (ETH)", color='#5ca6ce')

plt.title("Bitcoin and Ethereum Percent Change (Last Two Quarters)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Percent Change (%)", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
    """},
#######################################################
# Example 5 - Updated Format
#######################################################
    {'role':'user','content':"Please plot the percent change of Bitcoin and Ethereum for the last two weeks. Can you show average growth across the portfolio using a line of best fit?"},
    {'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename  # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbols for Bitcoin and Ethereum
symbols = ["BTC-USD", "ETH-USD"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as two weeks ago
start_date = end_date - timedelta(days=14)

# Fetch the historical data for Bitcoin and Ethereum using yfinance
data = yf.download(symbols, start=start_date, end=end_date)

# Calculate the percent change for Bitcoin and Ethereum. Must drop na.
percent_change = data["Close"].pct_change().dropna() * 100

# Set a custom color palette for Bitcoin (orange) and Ethereum (light blue)
colors = ['#FFA500', '#ADD8E6']

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Find regression data for the group
regression_data = data[data.index >= end_date - timedelta(days=7)]['Close'].pct_change().dropna().melt(var_name="Symbol",value_name="percent_change",ignore_index=False)
X = regression_data.index.to_frame()
X_numeric = np.arange(len(X))  # Convert dates to numeric values
y = regression_data.percent_change
regressor = LinearRegression()
regressor.fit(X_numeric.reshape(-1, 1), y)

# Start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the percent change for Bitcoin and Ethereum for the past two weeks
plt.plot(percent_change.index, percent_change["BTC-USD"], label="Bitcoin (BTC)", color='#FFA500')
plt.plot(percent_change.index, percent_change["ETH-USD"], label="Ethereum (ETH)", color='#ADD8E6')

# Plot the regression model
predicted_prices = regressor.predict(X_numeric.reshape(-1,1))
plt.plot(X,predicted_prices,color='lime',linestyle='--',label='Group Average')

plt.title("Bitcoin and Ethereum Percent Change (Last Two Weeks)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Percent Change (%)", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
#######################################################
# Example 6 - Updated Format
#######################################################
    {
    'role':'user','content':"Can you plot Verizon's stock price over the year? Can you add a line of best fit for the past quarter? Use a white theme and make the graph red 📈. Can you annotate the chart with information about the line of best fit?"
    },{
        'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename  # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Verizon
ticker = "VZ"

# Get today's date
end_date = datetime.today()

# Calculate the start date as one year ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Verizon using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the start date as one quarter (three months) ago
start_date_one_quarter_ago = end_date - timedelta(days=91)

# Filter the historical data for Verizon for the past quarter
data_one_quarter = data[data.index.to_series() > start_date_one_quarter_ago]

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Verizon over the past year
plt.plot(data.index, data["Close"], label="Verizon", color='red')

# Calculate the numerical values for X (dates) and Y (closing prices)
X = pd.DataFrame((data_one_quarter.index - start_date_one_quarter_ago).days)
y = pd.Series(data_one_quarter["Close"])

# Fit a linear regression model
regressor = LinearRegression()
regressor.fit(X, y)

# Predict the stock prices using the linear regression model
predicted_prices = regressor.predict(X)

# Plot the linear regression line for the past quarter
plt.plot(data_one_quarter.index, predicted_prices, color='black', linestyle='--', label='Linear Regression')

plt.title("Verizon Stock Price (Past Year)", fontsize=16, fontweight='bold', color="black")
plt.xlabel("Date", fontsize=14, color="black")
plt.ylabel("Stock Price (USD)", fontsize=14, color="black")
plt.legend()

plt.tight_layout()

plt.savefig(filename, dpi=300, bbox_inches='tight')
        """
    }
#######################################################
# Example 7
#######################################################
]