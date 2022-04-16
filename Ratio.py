import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import pytz
from random import sample
# import hvplot.pandas 

def sharpe_rate(df):
    sharpe_ratios = (df.mean() * 730) / (df.std() * np.sqrt(730))
    # return sharpe_ratios
    sp = sharpe_ratios.plot.bar(figsize=(20,10),title = "Sharpe Ratio for All Token")
    # sp.show()
    return sp, sharpe_ratios
    

def beta(main,brenchmark,period):
    covariance = main.rolling(window=period).cov(brenchmark)
    variance = brenchmark.rolling(window=period).var()
    beta = covariance / variance
    return beta

def markowitz(df):

    years = 2
    returns = df.pct_change()
    cagr = (df.iloc[-1] / df.iloc[0]) ** (1 / years) - 1
    cov = returns.cov()
    def random_weights(n):
        k = np.random.rand(n)
        return k / sum(k)
    exp_return = 0
    sigma = 0
    
    for _ in range(1):
        w = random_weights(len(df.columns))
        exp_return = np.dot(w, cagr.T)
        sigma = (np.sqrt(np.dot(np.dot(w.T, cov), w)))
        
    return sigma, exp_return
    
    # plt.plot(sigma, exp_return, 'ro', alpha=0.1)
    # plt.show()

def plot_MC(df,name, num_days): 
    #df = get_data(ticker, start_date, end_date)
    initial_price = 125 #df.iloc[-1].values[0]

    pct_changes = df.pct_change()
    pct_changes.dropna(inplace=True)
    pct_changes.index = pd.to_datetime(pct_changes.index)

    possible_changes = list(pct_changes.values)


    plt.figure(figsize=(20,10))

    realizations = []
    for i in range(0, 500): 

        current_price = initial_price 
        current_price_history = []
        for i in range(num_days): 
            current_pct_change = sample(possible_changes,1)[0]
            current_price = current_price * (1+ current_pct_change)
            current_price_history.append(current_price)


        plt.plot(current_price_history)
        plt.title(f"Monte Carlo Simulation for {name}")

        realizations.append(current_price_history)

    plt.show()    

    closing_prices_as_of_last_day = [x[-1] for x in realizations]
    expected_return = (np.mean(closing_prices_as_of_last_day) - initial_price)/initial_price
    low_bound =  np.mean(closing_prices_as_of_last_day)  - 2*np.std(closing_prices_as_of_last_day)
    upper_bound =  np.mean(closing_prices_as_of_last_day)  + 2*np.std(closing_prices_as_of_last_day)

    print(f"The iniital investment was {initial_price}")
    print(f"The expected return on {name} is {expected_return} will be between {low_bound} and {upper_bound} with 95% confidence in the next {num_days} trading days")
    return low_bound, upper_bound
    
    

    #low_bound =  np.mean(closing_prices_as_of_last_day)  - 1*np.std(closing_prices_as_of_last_day)
    #upper_bound =  np.mean(closing_prices_as_of_last_day)  + 1*np.std(closing_prices_as_of_last_day)

    #print(f"The starting closing price at the end of this period was {initial_price}")
    #print(f"The expected return on {name} is {expected_return} and the closing price will be between {low_bound} and {upper_bound} with 67% confidence in the next {num_days} trading days")