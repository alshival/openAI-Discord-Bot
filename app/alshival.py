{'role':'user','content':"Plot Apple, Google, Meta, and Microsofit's stock price on a chart. Standardize the results and add a line of best fit for the group. Use playful colors and a large font for the title. Make the font for the axis text larger as well."},
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

tickers = ["AAPL", "GOOGL", "FB", "MSFT"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as one year ago from today
start_date = end_date - timedelta(days=365)

# Fetch the historical data for Apple, Google, Meta, and Microsoft using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Standardize the stock prices
standardized_data = (data - data.mean()) / data.std()

# Set a playful color palette
colors = ['#FF0000', '#00FF00', '#0000FF', '#FF00FF']
sns.set_palette(sns.color_palette(colors))

# Set plot style and size
plt.style.use('default')
plt.figure(figsize=(chart_width, chart_height))

# Plot the standardized stock prices for Apple, Google, Meta, and Microsoft
for ticker in tickers:
    plt.plot(standardized_data.index, standardized_data[ticker], label=ticker)

# Fit a linear regression model
X = np.arange(len(standardized_data)).reshape(-1, 1)
y = standardized_data.mean(axis=1).values
regressor = LinearRegression()
regressor.fit(X, y)

# Generate the line of best fit for the group
line_of_best_fit = regressor.predict(X)

# Plot the line of best fit
plt.plot(standardized_data.index, line_of_best_fit, 'k--', label='Line of Best Fit')

# Set plot labels and title
plt.xlabel("Date", fontsize=14)
plt.ylabel("Standardized Stock Price", fontsize=14)
plt.title("Standardized Stock Prices of Apple, Google, Meta, and Microsoft", fontsize=24, fontweight='bold')

# Set font size for tick labels
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Set legend
plt.legend()

# Save the plot as a .png image file
filename = "Stock_Prices_Apple_Google_Meta_Microsoft.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""}