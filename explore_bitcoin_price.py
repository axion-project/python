# Explore Bitcoin Price Data in Python
# By Michael Morales

import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Function to fetch Bitcoin price data from CoinGecko API
def fetch_bitcoin_data():
    """
    Fetches the historical Bitcoin price data from the CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': '30',  # Get data for the last 30 days
        'interval': 'daily'
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['prices']
    else:
        print("Failed to fetch data from CoinGecko API.")
        return []

# Function to process the raw data into a pandas DataFrame
def process_data(raw_data):
    """
    Converts the raw Bitcoin price data into a pandas DataFrame.
    """
    # Create a DataFrame from the raw price data
    df = pd.DataFrame(raw_data, columns=['timestamp', 'price'])
    
    # Convert timestamp into a readable date
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    # Set the date as the index
    df.set_index('date', inplace=True)
    
    return df

# Function to plot Bitcoin price data
def plot_bitcoin_prices(df):
    """
    Plots the Bitcoin price data over time.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['price'], label='Bitcoin Price (USD)', color='orange')
    plt.title('Bitcoin Price Over the Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function to perform basic analysis on the data
def analyze_bitcoin_data(df):
    """
    Prints basic statistics and analysis on the Bitcoin price data.
    """
    # Basic statistics
    print("\nBasic Statistics for Bitcoin Prices:")
    print(df.describe())
    
    # Calculate the daily price change (percentage)
    df['daily_change'] = df['price'].pct_change() * 100
    
    # Calculate the highest and lowest price in the last 30 days
    max_price = df['price'].max()
    min_price = df['price'].min()
    
    print(f"\nHighest Bitcoin Price in the Last 30 Days: ${max_price:.2f}")
    print(f"Lowest Bitcoin Price in the Last 30 Days: ${min_price:.2f}")
    
    # Print the average daily price change
    avg_daily_change = df['daily_change'].mean()
    print(f"\nAverage Daily Change in Bitcoin Price: {avg_daily_change:.2f}%")

# Main function to execute the script
def main():
    print("Fetching Bitcoin price data...")
    
    # Fetch Bitcoin price data
    raw_data = fetch_bitcoin_data()
    
    if raw_data:
        # Process the data into a DataFrame
        df = process_data(raw_data)
        
        # Perform basic analysis
        analyze_bitcoin_data(df)
        
        # Plot the Bitcoin price data
        plot_bitcoin_prices(df)

# Run the script
if __name__ == "__main__":
    main()
