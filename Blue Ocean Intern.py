import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# Read Weather Data for Mumbai (2 years)
# Path in my device
weather_data = pd.read_csv(r'C:\Users\ahmad\Downloads\mumbai.csv')

# Read Stock Market Data (NSE Index - 5 years)
# Path in my device
stock_data = pd.read_csv(r'C:\Users\ahmad\Downloads\^NSEI-2.csv')


# Process for Data Analysis
# Removing the NULL values if present in row
weather_data = weather_data.dropna()

#Removing the NULL values if present in row
stock_data = stock_data.dropna()

# Scatter Plot Graph

# Making graphs to Visualize weather data using line plots and identify trends over time
plt.figure(figsize=(10, 6))
plt.plot(weather_data['date_time'], weather_data['tempC'], label='Temperature')
plt.plot(weather_data['date_time'], weather_data['humidity'], label='Humidity')
plt.plot(weather_data['date_time'], weather_data['windspeedKmph'], label='Wind Speed')
plt.xlabel('Date Time')
plt.ylabel('Value')
plt.title('Weather Data for Mumbai')
plt.legend()
plt.show()


# Making a graph for Stock Analysis taking Stock Price and Trading Volume
# Stock price is take as Close and trading volume as Volume
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Date'], stock_data['Close'], label='Stock Price')
plt.plot(stock_data['Date'], stock_data['Volume'], label='Trading Volume')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Stock Analysis')
plt.legend()
plt.show()


# Correlation Analysis
# precipMM = precipetation, tempC = Temperature
weather_variables = ['date_time', 'humidity', 'precipMM' ,'tempC', 'windspeedKmph']
stock_variables = ['Open', 'High', 'Low' , 'Close', 'Volume']

# Checking if the selected weather variables exist in the weather data
if set(weather_variables).issubset(weather_data.columns):
    # Calculate correlation coefficients
    correlation_matrix = weather_data[weather_variables].corrwith(stock_data[stock_variables], numeric_only=True)
    print(correlation_matrix)
    
    # Correlation matrix (Heatmap)
    plt.figure(figsize=(8, 6))
    plt.imshow(correlation_matrix.values.reshape(1, -1), cmap='coolwarm', aspect='auto')
    plt.xticks(ticks=range(len(weather_variables) + len(stock_variables)), labels=weather_variables + stock_variables, rotation=45, ha='right')
    plt.yticks([])
    plt.colorbar()
    plt.title('Correlation Matrix between Weather and Stock Variables')
    plt.show()
else:
    print("Selected weather variables do not exist in the weather data.")

# Processing Monte Carlo Simulation
# Parameters(Standard)
iterations = 1000
investment_amount = 1000
risk_tolerance = 0.02

# Investment performance(Final value recieved)
investment_values = []
for _ in range(iterations):

    # Generate random weather conditions (sample from weather data)
    random_weather = weather_data.sample(1)
    
    # Generate random stock market performance values (sample from stock data)
    random_stock = stock_data.sample(1)
    
    # Investment value based on stock market performance

    
    # Return Ratio = {(closing price/ opening price) -1}
    random_stock_return = np.random.choice(stock_data['Close'] / stock_data['Open'] - 1)
    
    # Formula: [Investment value = Amount invested x {1+ (Return ratio)} x (ratio depicting no risk )
    investment_value = investment_amount * (1 + random_stock_return) * (1 - risk_tolerance)
    investment_values.append(investment_value)


# Analyze simulated investment performance
mean_investment = np.mean(investment_values)
std_investment = np.std(investment_values)

# Investment distribution(labels)
# Matplotlib Histogram
# Frequency refers to the number of occurrences of each investment value 
plt.hist(investment_values, bins=30)
plt.xlabel('Final Investment Value')
plt.ylabel('Frequency')
plt.title('Result')
plt.show()


# Print mean and standard deviation of investment values

print('Mean Investment Value: $', round(mean_investment, 2))
print('Standard Deviation of Investment Value: $', round(std_investment, 2))