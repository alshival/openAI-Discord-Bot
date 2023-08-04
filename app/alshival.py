{'role':'user','content':"Plot Apple, Google, META, and Microsoft's stock price for the past 5 years. Approximate the group average using polynomials of degree 2, 3, and 4. Use a white background and playful colors. Large title please."},
{'role':'assistant','content':"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# DO NOT CHANGE THIS SECTION
chart_width = 12
chart_height = 8

tickers = ["AAPL", "GOOGL", "META", "MSFT"]

# Get today's date
end_date = datetime.today()

# Calculate the start date as five years ago from today
start_date = end_date - timedelta(days=5*365)

# Fetch the historical data for Apple, Google, META, and Microsoft using yfinance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Set a custom color palette
colors = ['#FF6B00', '#1A8CFF', '#FF00FF', '#00FF00']
sns.set_palette(sns.color_palette(colors))

# Standardize the stock prices of each company
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Set white background theme for the plot using Matplotlib
plt.style.use('default')

# Plot the stock prices for Apple, Google, META, and Microsoft for the past five years
plt.figure(figsize=(chart_width, chart_height))
for i, ticker in enumerate(tickers):
    plt.plot(data.index, scaled_data[:, i], label=ticker)

# Calculate the group average using polynomials of degree 2, 3, and 4
X = np.arange(len(data)).reshape(-1, 1)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)
regressor = LinearRegression()
regressor.fit(X_poly, scaled_data.mean(axis=1).reshape(-1, 1))
y_poly_pred = regressor.predict(X_poly)
plt.plot(data.index, y_poly_pred, color='black', linestyle='--', label='Group Average (Degree 2)')

poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(X)
regressor.fit(X_poly, scaled_data.mean(axis=1).reshape(-1, 1))
y_poly_pred = regressor.predict(X_poly)
plt.plot(data.index, y_poly_pred, color='gray', linestyle='--', label='Group Average (Degree 3)')

poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
regressor.fit(X_poly, scaled_data.mean(axis=1).reshape(-1, 1))
y_poly_pred = regressor.predict(X_poly)
plt.plot(data.index, y_poly_pred, color='silver', linestyle='--', label='Group Average (Degree 4)')

# Set plot labels and title
plt.xlabel("Date")
plt.ylabel("Stock Price (Standardized)")
plt.title("Stock Prices of Apple, Google, META, and Microsoft (Last 5 Years)", fontsize=20)

# Set legend
plt.legend()

# Save the plot as an image file
filename = "Stock_Prices_5_Years.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()
"""}