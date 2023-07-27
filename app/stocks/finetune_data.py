finetune = [
{'role':'user','content':"Can you create a candlestick chart of Tesla's stock price with volume bars for the past six months."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename  # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Tesla
ticker = "TSLA"

# Get today's date
end_date = datetime.today()

# Calculate the start date as six months ago from today
start_date = end_date - timedelta(days=180)

# Fetch the historical data for Tesla using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Tesla's brand colors
colors = ['#E82127', '#FABD42', '#6E6E6E', '#BFBFBF']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the candlestick chart for Tesla stock price for the past six months
mpf.plot(data, type='candle', style='yahoo', title="Tesla Stock Price (Last Six Months)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'), volume=True)
plt.close()
"""},{'role':'user','content':"Can you create a candlestick chart of Microsoft's stock price for the past three quarters? Add bars for volume as well."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Microsoft
ticker = "MSFT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as three quarters (nine months) ago
start_date = end_date - timedelta(days=270)

# Fetch the historical data for Microsoft using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Microsoft's brand colors
colors = ['#3C6EB4', '#FFB900', '#B4009E', '#00A300']
sns.set_palette(sns.color_palette(colors))

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# Plot the candlestick chart for Microsoft stock price for the past three quarters
mpf.plot(data, type='candle', style='yahoo', title="Microsoft Stock Price (Last Three Quarters)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'))

plt.close()  # Close the figure to prevent it from being displayed inline

print(f"Plot saved as {filename}")
"""},
{'role':'user','content':"Can you create a candlestick chart for Apple's stock price in the past 128 days? Add bars for volume."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename  # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Microsoft
ticker = "AAPL"

# Get today's date
end_date = datetime.today()

# Calculate the start date as 128 days ago from today
start_date = end_date - timedelta(days=128)

# Fetch the historical data for Apple using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Apple's brand colors
colors = ['#b6b6b6', '#999999', '#e9e9e9', '#d8d8d8']
sns.set_palette(sns.color_palette(colors))

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# Plot the candlestick chart for Microsoft stock price for the past three quarters
mpf.plot(data, type='candle', style='yahoo', title="Apple Stock Price (Last 128 days)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'), volume=True)
plt.close()
"""},
{'role':'user','content':"can you plot percent price change for bitcoin, ethereum, and dogecoin for the past three quarters? Use a dark theme, orange for bitcoin, light blue for ethereum, and yellow for dogecoin."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbols for Bitcoin, Ethereum, and Dogecoin
tickers = ["BTC-USD", "ETH-USD", "DOGE-USD"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as three quarters (nine months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Bitcoin, Ethereum, and Dogecoin using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Calculate the percent change for each cryptocurrency
percent_change = data.pct_change()

# Set a dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the percent change for Bitcoin, Ethereum, and Dogecoin for the past three quarters
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.plot(percent_change.index, percent_change[tickers[0]], label="Bitcoin", color='orange')
plt.plot(percent_change.index, percent_change[tickers[1]], label="Ethereum", color='lightblue')
plt.plot(percent_change.index, percent_change[tickers[2]], label="Dogecoin", color='yellow')

plt.title("Percent Change in Cryptocurrency Prices (Last Three Quarters)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Percent Change", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"can you plot the price of Microsoft and Apple together? Can you add a line of best fit for the pair?"},
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

# Define the ticker symbols for Microsoft and Apple
tickers = ["MSFT", "AAPL"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Microsoft and Apple using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Set a custom color palette inspired by Microsoft and Apple's brand colors
colors = ['#3C6EB4', '#FFB900']
sns.set_palette(sns.color_palette(colors))

# Calculate the start date as two quarters (six months) ago
start_date_two_quarters_ago = end_date - timedelta(days=182)

# Filter the historical data for Microsoft and Apple for the past two quarters 
data_two_quarters = data[data.index.to_series() > start_date_two_quarters_ago]

# Take our dates as X. Convert datetime to numerical values.
X = pd.DataFrame((data_two_quarters.index - start_date_two_quarters_ago).days)

# Take the average of the "Close" prices for Microsoft and Apple as Y
y = pd.Series(data_two_quarters.mean(axis=1))

# Fit a linear regression model
regressor = LinearRegression()
regressor.fit(X, y)

# Predict the stock prices using the linear regression model
predicted_prices = regressor.predict(X)

# Set fivethirtyeight background theme for the plot using Matplotlib
plt.style.use('fivethirtyeight')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Microsoft and Apple for the past two quarters
plt.plot(data.index, data[tickers[0]], label="Microsoft (MSFT)")
plt.plot(data.index, data[tickers[1]], label="Apple (AAPL)")

# Plot the linear regression line
plt.plot(data_two_quarters.index, predicted_prices, color='red', linestyle='--', label='Linear Regression')

plt.title("Microsoft and Apple Stock Prices (Last Two Quarters)", fontsize=16, fontweight='bold', color="#333333")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"can you plot Krispy Kreme's stock price for the past six months, as well as a regression line. Do not show volume and do not use candlesticks."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
import statsmodels.api as sm

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Krispy Kreme
ticker = "DNUT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as six months ago from today
start_date = end_date - timedelta(days=180)

# Fetch the historical data for Krispy Kreme using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Krispy Kreme's brand colors
colors = ['#FFB900', '#DD1100']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the stock price for Krispy Kreme for the past six months
plt.figure(figsize=(chart_width, chart_height))
plt.plot(data['Close'], label="Stock Price")

# Generate regression line
X = np.arange(len(data)).reshape(-1, 1)
X = sm.add_constant(X)
y = data['Close'].values
model = sm.OLS(y, X).fit()
regression_line = model.predict(X)
plt.plot(data.index, regression_line, 'r--', label="Regression Line")

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Krispy Kreme Stock Price (Last Six Months)")

# Set legend
plt.legend()

# Save the plot as an image file
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()

print(f"Plot saved as {filename}")
"""},
{'role':'user','content':"can you plot the price of Microsoft and Apple together? Can you add a line of best fit for each? Furthermore, can you add information about the lines of best fit?"},
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

# Define the ticker symbols for Microsoft and Apple
tickers = ["MSFT", "AAPL"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as four quarters (three months) ago
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Microsoft and Apple using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Set a custom color palette
colors = ['#3C6EB4', '#FFB900']
sns.set_palette(sns.color_palette(colors))

# Calculate the start date as two quarters (six months) ago
start_date_two_quarters_ago = end_date - timedelta(days=182)

# Filter the historical data for Microsoft and Apple for the past two quarters 
data_two_quarters = data[data.index.to_series() > start_date_two_quarters_ago]

# Take our dates as X. Convert datetime to numerical values.
X = pd.DataFrame((data_two_quarters.index - start_date_two_quarters_ago).days)

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Microsoft and Apple for the past two quarters
plt.plot(data.index, data[tickers[0]], label="Microsoft (MSFT)")
plt.plot(data.index, data[tickers[1]], label="Apple (AAPL)")

# Fit a linear regression model for Microsoft
regressor_msft = LinearRegression()
regressor_msft.fit(X, data_two_quarters[tickers[0]])

# Fit a linear regression model for Apple
regressor_aapl = LinearRegression()
regressor_aapl.fit(X, data_two_quarters[tickers[1]])

# Predict the stock prices using the linear regression models
predicted_prices_msft = regressor_msft.predict(X)
predicted_prices_aapl = regressor_aapl.predict(X)

# Plot the linear regression lines
plt.plot(data_two_quarters.index, predicted_prices_msft, color='red', linestyle='--', label='MSFT Linear Regression')
plt.plot(data_two_quarters.index, predicted_prices_aapl, color='blue', linestyle='--', label='AAPL Linear Regression')

# Add information about the lines of best fit
plt.annotate(f"MSFT: {regressor_msft.coef_[0]:.2f}", xy=(data_two_quarters.index[-1], predicted_prices_msft[-1]), xytext=(data_two_quarters.index[-1] - pd.DateOffset(months=1), predicted_prices_msft[-1]), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate(f"AAPL: {regressor_aapl.coef_[0]:.2f}", xy=(data_two_quarters.index[-1], predicted_prices_aapl[-1]), xytext=(data_two_quarters.index[-1] - pd.DateOffset(months=1), predicted_prices_aapl[-1]), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.title("Microsoft and Apple Stock Prices (Last Two Quarters)", fontsize=16, fontweight='bold', color="#333333")
plt.xlabel("Date", fontsize=14, color="#333333")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#333333")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"can you plot Disney's volume for the past two blood moons?"},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Disney
ticker = "DIS"

# Get today's date
end_date = datetime.today()

# Calculate the start date as two blood moons (approximately 59 days) ago
start_date = end_date - timedelta(days=59)

# Fetch the historical data for Disney using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the "Volume" for Disney for the past two blood moons
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.plot(data.index, data["Volume"], color='cyan')  # Change color to cyan

plt.title("Disney Stock Volume (Past Two Blood Moons)", fontsize=16, fontweight='bold', color="#FFFFFF")  # Change color to white
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Volume", fontsize=14, color="#FFFFFF")

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"can you plot Disney's volume for the past two blood moons? Use bars and a white background."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Disney
ticker = "DIS"

# Get today's date
end_date = datetime.today()

# Calculate the start date as two blood moons (approximately 59 days) ago
start_date = end_date - timedelta(days=59)

# Fetch the historical data for Disney using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the volume for Disney for the past two blood moons using bars
fig, ax = plt.subplots(figsize=(chart_width, chart_height))
plt.bar(data.index, data["Volume"], color='blue')

plt.title("Disney Stock Volume (Past Two Blood Moons)", fontsize=16, fontweight='bold', color="#000000")
plt.xlabel("Date", fontsize=14, color="#333333")
plt.ylabel("Volume", fontsize=14, color="#333333")

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"can you plot Disney's stock price for the past 28 days? Also include bars for volume."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Disney
ticker = "DIS"

# Get today's date
end_date = datetime.today()

# Calculate the start date as 28 days ago
start_date = end_date - timedelta(days=28)

# Fetch the historical data for Disney using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Disney's brand colors
colors = ['#0033CC', '#FF9900']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Plot the "Close" price for Disney for the past 28 days
plt.plot(data.index, data["Close"], label="Disney (DIS)")

# Add bars for volume
ax2 = ax.twinx()
ax2.bar(data.index, data["Volume"], alpha=0.3, width=0.5, align='center', color='#FF9900', label="Volume")

plt.title("Disney Stock Price (Past 28 Days)", fontsize=16, fontweight='bold', color="#FFFFFF")
plt.xlabel("Date", fontsize=14, color="#FFFFFF")
plt.ylabel("Stock Price (USD)", fontsize=14, color="#FFFFFF")
ax2.set_ylabel("Volume", fontsize=14, color="#FFFFFF")
plt.legend()

plt.tight_layout()  # Adjust plot layout for better spacing

plt.savefig(filename, dpi=300, bbox_inches='tight')
"""},
{'role':'user','content':"can you plot Microsoft's stock price for the past three quarters using candlesticks?"},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Microsoft
ticker = "MSFT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as three quarters (nine months) ago
start_date = end_date - timedelta(days=365*0.75)

# Fetch the historical data for Microsoft using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Microsoft's brand colors
colors = ['#3C6EB4', '#FFB900', '#B4009E', '#00A300']
sns.set_palette(sns.color_palette(colors))

# Plot the candlestick chart for Microsoft for the past three quarters
mpf.plot(data, type='candle', style='yahoo', title="Microsoft Stock Price (Last Three Quarters)",
         ylabel="Stock Price (USD)", figsize=(chart_width, chart_height), savefig=filename)
"""},
{'role':'user','content':"can you plot Krispy Kreme's stock price for the past six months, as well as volume?"},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import mplfinance as mpf

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8
filename = filename # DO NOT CHANGE. WILL BE COMPILED.

# Define the ticker symbol for Krispy Kreme
ticker = "DNUT"

# Get today's date
end_date = datetime.today()

# Calculate the start date as six months ago from today
start_date = end_date - timedelta(days=180)

# Fetch the historical data for Krispy Kreme using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Set a custom color palette inspired by Krispy Kreme's brand colors
colors = ['#FF7900', '#E9A600', '#D6D6D6']
sns.set_palette(sns.color_palette(colors))

# Set dark background theme for the plot using Matplotlib
plt.style.use('dark_background')

# Plot the candlestick chart for Krispy Kreme stock price for the past six months
mpf.plot(data, type='candle', style='yahoo', title="Krispy Kreme Stock Price (Last Six Months)", ylabel="Stock Price (USD)",
         figsize=(chart_width, chart_height), savefig=dict(fname=filename, dpi=300, bbox_inches='tight'), volume=True)
plt.close()

print(f"Plot saved as {filename}")
"""}
]