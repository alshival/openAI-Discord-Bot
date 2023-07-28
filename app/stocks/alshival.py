{'role':'user','content':"can you plot Match Group, Bumble, and Hello Group (NASDAQ:MOMO) for the past two years? Add a line of regression for the past year for each symbol and information about the regression lines. Use a white theme, blue for match group, orange for bumble, and green for hello group."},
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

tickers = ["MTCH", "BMBL", "MOMO"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as two years ago from today
start_date = end_date - timedelta(days=365*2)

# Fetch the historical data for each symbol using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Set a custom color palette for each symbol
colors = ['#003399', '#FF9900', '#00CC66']
sns.set_palette(sns.color_palette(colors))

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# Create a list to store regression line information
regression_info = []

# Start figure
fig, ax = plt.subplots(figsize=(chart_width, chart_height))

# Iterate through each symbol and plot the closing price
for i, ticker in enumerate(tickers):
    # Plot the closing price
    plt.plot(data.index, data[ticker], label=ticker)
    
    # Perform linear regression for the past year
    X = np.arange(len(data[ticker].values[-365:])).reshape(-1, 1)
    y = data[ticker].values[-365:].reshape(-1, 1)
    reg = LinearRegression().fit(X, y)
    
    # Store regression line information
    slope = reg.coef_[0][0]
    intercept = reg.intercept_[0]
    regression_info.append((ticker, slope, intercept))
    
    # Plot the regression line
    plt.plot(data.index[-365:], reg.predict(X), linestyle='--', linewidth=2)

# Add legend and title
plt.legend()
plt.title("Stock Price for Match Group, Bumble, and Hello Group (Past Two Years)", fontsize=16, fontweight='bold')

# Add information about the regression lines
for info in regression_info:
    symbol, slope, intercept = info
    plt.text(data.index[-400], data[symbol].values[-1], f"{symbol}: y = {slope:.2f}x + {intercept:.2f}", fontsize=12)

# Save the image as a .png file
filename = "Stock_Price_Regression.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""}