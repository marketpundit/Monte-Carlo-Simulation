#Libraries required to perform the task.
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

#Stock price history timeframe.
start = dt.datetime(2017, 1, 3)
end = dt.datetime(2019, 11, 8)

#Stock ticker and DataSource (Yahoo). Trading session sctock's Close Price
prices = web.DataReader('AMD', 'yahoo', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

#Number of Simulations 1K. Looking into 252 days out into the future.
num_simulations = 1000
num_days = 252

#Creating DataFrame for Simulation Output.
simulation_df = pd.DataFrame()

#Monte Carlo Simulation Model.
for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
        
    simulation_df[x] = price_series

#Visualizing Simulation Results 
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: AMD')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()