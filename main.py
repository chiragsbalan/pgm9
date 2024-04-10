import pandas as pd
import matplotlib.pyplot as plt

#Company Data
# Load data from CSV file
df = pd.read_csv('datasets/sp500_companies.csv')
# Calculate the count of companies in each sector
sector_counts = df['Sector'].value_counts()
# Define colors for the pie chart sections
colors = plt.cm.tab20.colors  # Using a color map for variety
# Plotting the pie chart with borders
plt.figure(figsize=(8, 6))
plt.pie(sector_counts, labels=sector_counts.index, autopct='%1.1f%%', startangle=140,
        colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
plt.tight_layout()
plt.savefig('static/sector.png')


# Load data from CSV file
df_companies = pd.read_csv('datasets/sp500_companies.csv')
# Sort companies by market cap in descending order
df_companies_sorted = df_companies.sort_values(by='Marketcap', ascending=False)
# Select top N companies for the bar chart
top_n = 10
top_companies = df_companies_sorted.head(top_n)
# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_companies['Shortname'], top_companies['Marketcap'], color='skyblue', edgecolor='black')
plt.xlabel('Company')
plt.ylabel('Market Cap (Billions)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Remove borders from the figure
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# Save the plot
plt.savefig('static/marketcap.png')


# Load data from CSV file
df_companies = pd.read_csv('datasets/sp500_companies.csv')
# Count the number of companies per stock exchange
exchange_counts = df_companies['Exchange'].value_counts()
# Sorting the exchanges based on the number of companies
sorted_exchanges = exchange_counts.sort_values(ascending=True)
# Plotting the horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(sorted_exchanges.index, sorted_exchanges.values, color='yellow', edgecolor='black')
plt.xlabel('Number of Companies')
plt.ylabel('Exchange Code')
plt.tight_layout()
# Remove borders from the figure
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# Save the plot
plt.savefig('static/exchanges.png')



#Stocks Data
# Load the dataset
df_stocks = pd.read_csv('datasets/sp500_stocks.csv')
# Convert 'Date' column to datetime
df_stocks['Date'] = pd.to_datetime(df_stocks['Date'])
# Extract year from 'Date' and create a new column
df_stocks['Year'] = df_stocks['Date'].dt.year
# Group by year and calculate average stock price
avg_prices_yearly = df_stocks.groupby('Year')['Adj Close'].mean()
# Plotting the average stock prices over years
plt.figure(figsize=(10, 6))
avg_prices_yearly.plot(kind='line', marker='o', color='green')
plt.xlabel('Year')
plt.ylabel('Average Stock Price (in Dollars)')
plt.tight_layout()
# Remove borders from the figure
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# Save the plot
plt.savefig('static/prices.png')


# Load the dataset
df_stocks = pd.read_csv('datasets/sp500_stocks.csv')
# Group by company symbol and sum the volume
volume_by_company = df_stocks.groupby('Symbol')['Volume'].sum()
# Sort companies by total volume in descending order
top_companies_volume = volume_by_company.sort_values(ascending=False).head(10)
# Plotting the most traded companies by volume
plt.figure(figsize=(10, 6))
top_companies_volume.plot(kind='bar', color='darkblue', edgecolor='black')
plt.xlabel('Company Symbol')
plt.ylabel('Total Volume')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Remove borders from the figure
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# Save the plot
plt.savefig('static/volume.png')


# Load the dataset
df_stocks = pd.read_csv('datasets/sp500_stocks.csv')
# Convert 'Date' column to datetime format
df_stocks['Date'] = pd.to_datetime(df_stocks['Date'])
# Extract the year from the 'Date' column
df_stocks['Year'] = df_stocks['Date'].dt.year
# Filter the DataFrame for the years 2010 to 2024
df_filtered = df_stocks[(df_stocks['Year'] >= 2010) & (df_stocks['Year'] <= 2024)]
# Calculate the average opening, high, low, and closing prices
avg_open = df_filtered.groupby('Year')['Open'].mean().values
avg_high = df_filtered.groupby('Year')['High'].mean().values
avg_low = df_filtered.groupby('Year')['Low'].mean().values
avg_close = df_filtered.groupby('Year')['Close'].mean().values
# Create the stack plot
plt.figure(figsize=(10, 6))
years = df_filtered['Year'].unique()  # Get the unique years for x-axis
plt.stackplot(years, avg_open, avg_high, avg_low, avg_close, labels=['Open', 'High', 'Low', 'Close'])
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.legend(loc='upper left')
plt.tight_layout()
# Remove borders from the figure
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# Save the plot
plt.savefig('static/stacked.png')




