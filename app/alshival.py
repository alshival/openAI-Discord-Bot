{'role':'user','content':"plot Google, Apple, Microsoft, and Meta's stock price for the past five years. Add polynomial approximations of degrees 2, 3, and 4 to estimate the group average. Use a white theme and color each line using brand colors."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import statsmodels.api as sm

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["GOOGL", "AAPL", "MSFT", "META"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as five years ago from today
start_date = end_date - timedelta(days=365*5)

# Fetch the historical data for Google, Apple, Microsoft, and Meta using yfinance
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Set custom color palettes for each stock
colors = ['#4285F4', '#FF3B30', '#7CBB00', '#FF6600']
sns.set_palette(sns.color_palette(colors))

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the stock prices for Google, Apple, Microsoft, and Meta for the past five years
plt.figure(figsize=(chart_width, chart_height))
for ticker in tickers:
    plt.plot(data[ticker], label=ticker)

# Generate polynomial approximations of degrees 2, 3, and 4 to estimate the group average
x = np.arange(len(data))
y = data.mean(axis=1)
degree = [2, 3, 4]
for d in degree:
    coefficients = np.polyfit(x, y, d)
    polynomial = np.poly1d(coefficients)
    plt.plot(data.index, polynomial(x), '--', linewidth=2)

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("Stock Prices for Google, Apple, Microsoft, and Meta (Last Five Years)")

# Set legend
plt.legend()

# Save the plot as an image file
filename = "Stock_Prices.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""}