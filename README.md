# PROJECT OVERVIEW 

A cryptocurrency is a digital currency that serves as a store of value and medium of exhange through an online network that is not regulated by the government and uses blockchain technologies to track the transactions. DeFi or Decentralized Finance, refers to a financial system that has no central powers or authority.

Since Bitcoin's release in 2009, cryptocurrencies have gained popularity and are now used as a common method of payment.

Creating a product for a blockchain requires several steps, one being to recognize which platform is most suitable for the product, given trends, market conditions, prices and future projections.

For this project, we used Coingecko to gather data on 8 transaction tokens in hopes to identify which platform is the most rewarding, given the performance of their top transaction tokens. This evaluation tool can be used for those who are introducing products to the blockchain.

## Tokens to Analyze 
 
 * Solana
 * Tron
 * Cronos
 * Fantom
 * Ethereum
 * Binance
 * Poly
 * XRP

## QUESTIONS WE HOPE TO ANSWER

* Which token provides the highest returns?

* Which token is the least / most risky?

* Which token has better future projections?

* How do these compare to a benchmark?

* Based on these findings, which exchange would be most rewarding?



# THE TEAM 

Amira Ali | Jeff Zhang | Nadeem Hassan 

# Tools & Resoures 

## SOFTWARE & TECHNOLOGIES USED 


 <img width="269" alt="Screen Shot 2022-04-14 at 4 13 59 PM" src="https://user-images.githubusercontent.com/99091066/163468356-ae335e88-997a-4ee4-ae0b-e929787c7230.png">

  > Python, Jupyter Notebook, Coingecko API, Plotly for visualization purposes. 


## CUSTOM MADE FUNCTION
  >Rato.py, helper_functions.py

### Ratio.py
Ratio.py contained the following function:

 * Sharpe ratio
 * Beta
 * Efficient frontier (Markowitz bullet)
 * Monte Carlo Simulation

### helper_function.py
helper_function.py contained the function to convert the csv data into dataframe and used in the data_clean.ipynb.

# DATA 

We were limited by multiple factors when choosing which API to fetch our data from. We expolored several platforms however either the API was not readily available or it did not have data on the tokens we were analyzing. We found that Coingecko had all the data we needed to meet our objectives. 

In order to have a fair evaluation tool, we had to ensure we had sufficient data for each token and a general starting point. We tested the API with different dates and tokens to decide the length of our data. All of the tokens had sufficient data from 2020 onwards, thus we decided to use 2 years worth of data (April 2020 - April 2022 ) or 730 days. 

`pip install pycoingecko` and importing `CoinGeckoAPI` gave us access to the data we needed for the analysis. 

First, we pulled historical prices, market capitalization, and volumes for each token and converted those into DataFrames. 
The naming conventions are as follows: 

Solana (price, market cap, volume) : `solaprice`, `solMC` , `volsol`

Tron: `tronprice` , `tronMC`, `voltron`

Cronos: `cronprice` , `volcron`, `cronMC`

Fantom: `fantomprice`, `volfantom`, `fantomMC`

Ethereum: `ethprice`, `voleth`, `ethMC`

Binance: `bnbprice`, `volbnb`, `bnbmC`

Poly: `polyprice`, `volpoly`, `polyMC`

XRP: `ripprice`, `volrip`, `ripMC` ( The coingecko api ID for XRP is Ripple) 

An excerpt of the code below shows our method of calling the XRP price by its coingecko ID, expressed in the currency, and the number data points we needed. We then changed `historic_pricerip` into a dataframe and called the Prices and Time columns.

```python 
historic_pricerip = cg.get_coin_market_chart_by_id("ripple", "usd", 730)
ripprice=pd.DataFrame(historic_pricerip['prices'], columns=['Time','XRP Price'])
ripprice 
```

<img width="176" alt="Screen Shot 2022-04-16 at 2 56 21 PM" src="https://user-images.githubusercontent.com/99091066/163687927-6402565a-4cf0-44b1-a8f2-604d8f320375.png">






The prices, market cap, and volume data for each token was then converted to a CSV file and pushed to github for cleaning & analysis. This can be found in the Data folder.

The Prices, Market Cap, and Volume dataframes were all combined into one dataframe.

```python
all_vol_df = pd.concat([solana_vol_df, bnb_vol_df, cron_vol_df, eth_vol_df, fantom_vol_df, poly_vol_df, tron_vol_df,xrp_vol_df], axis = 1)
all_vol_df.dropna(inplace = True)
all_vol_df
``` 

<img width="702" alt="Screen Shot 2022-04-16 at 2 58 15 PM" src="https://user-images.githubusercontent.com/99091066/163687985-d4ea3f6b-fb4d-42c6-ac89-88f8715e9809.png">


```python 
all_MC_df = pd.concat([solana_MC_df, bnb_MC_df, cron_MC_df, eth_MC_df, fantom_MC_df, poly_MC_df, tron_MC_df,xrp_MC_df], axis = 1)
all_MC_df.dropna(inplace = True)
all_MC_df
```

<img width="701" alt="Screen Shot 2022-04-16 at 2 58 56 PM" src="https://user-images.githubusercontent.com/99091066/163688009-b5c27e6b-5a1c-459c-ba65-c42ec2a7592c.png">


```python 
all_coins_df = pd.read_csv('all_coins.csv')
all_coins_df.rename({'XRP Price': 'XRP', 'Solana Price': 'Solana', 'Tron Price': 'Tron', 'PolyMath Price': 'PolyMath', 'Fantom Price': 'Fantom'
                               , 'Ethereum Price': 'Ethereum', 'Cronos Price': 'Cronos', 'Binance Price': 'Binance'}, axis = 1, inplace=True)
all_coins_df
```

<img width="566" alt="Screen Shot 2022-04-16 at 3 00 21 PM" src="https://user-images.githubusercontent.com/99091066/163688047-e0ff653c-be1b-48cd-b25e-ea2637d02255.png">

  > We concatenated the data together and dropped null values. The combined dataframes were renamed as `all_coins_df`, `all_vol_df` , `all_MC_df`


### Volumes and Market Capitalization

Each token's price, volume, and market capitalization were plotted using plotly and exported to a dashboard that can be found in [here](https://github.com/bleachevil/Classwork/blob/c843ab0daab4022152c153559c40a695e285a966/Combining.ipynb)

Example : Solana

<img width="821" alt="Screen Shot 2022-04-16 at 3 04 23 PM" src="https://user-images.githubusercontent.com/99091066/163688168-63d79a7d-e3eb-4f04-b940-4c782f1b992a.png">

Both volume and market capitalization are important metrics when analyzing which token is suitable for each investor. 
Volumes indicate the activity and whether the token is being bought/sold. The quantity over two years was plotted. 

Market capitalization refers to the total value of each coin, calculated by the amount in circulation multiplied by the price.


# ANALYSIS

In order to compare the tokens, we constructed a balanced ETF to use as a benchmark. 
To do this, we used an arbitrary investment amount `$1000` and divided the investment amount equally amongst the tokens to get `125` per token. We then used `125` and divided this value by the closing prices for each token.

```python
# Number of coins per token for $125 investment in that token

d = {'ticker': tickers, 'coins': coins}
df = pd.DataFrame(data=d)
df.set_index('ticker', inplace=True)
df
```

<img width="139" alt="Screen Shot 2022-04-16 at 3 12 13 PM" src="https://user-images.githubusercontent.com/99091066/163688375-93e01079-bb62-476d-90c9-f3a5d55c2ac0.png">

```python
# create a portfolio value by multiplying the # of tokens to the closing price on that day. On day 1, it is exactly our initial investment of $1000.

sum_df = all_coins_df.mul(coins_df.iloc[0])
sum_df['Total'] = sum_df.sum(axis = 1)
sum_df
```

<img width="711" alt="Screen Shot 2022-04-16 at 3 13 16 PM" src="https://user-images.githubusercontent.com/99091066/163688402-16062428-63ac-4caa-88fa-776cc7f4ea2d.png">


For the first data point, April 11th, all tokens have an equal $125. Then depending on the fluctuation in token prices, the balanced ETF either increases or decreases according to the sum of the values. 


The balanced ETF column was combined with the `all_coins_df` dataframe.

```python
# Adding the sum_df dataframe to the all_coins df for benchmarking

all_coins_df['Balanced ETF'] = sum_df['Total']
all_coins_df
```


<img width="605" alt="Screen Shot 2022-04-16 at 3 15 30 PM" src="https://user-images.githubusercontent.com/99091066/163688448-14044c58-b8c7-4105-8d2f-9cb81922bb93.png">



### Risk & Return


<img width="784" alt="Screen Shot 2022-04-14 at 7 24 17 PM" src="https://user-images.githubusercontent.com/99091066/163492704-8b371c5b-1b78-4b0e-a8cd-02d1d3421248.png">

Each token was plotted on a graph showing its risk/return. Depending on the individual's objectives, one who is risk averse would select tokens with higher return given a lower risk. For this investor, tokens such as Tron would be a suitable investment. 
individuals with a higher risk appetite would prefer Fantom as it has the highest risk and return amongst the other tokens.

Based on this chart, XRP and Polymath would not be a good investmemt since they have a relatively large risk and lower return.


### Sharpe Ratios

Using the [ratio.py](https://github.com/bleachevil/Classwork/blob/f88b8ef9929a5e53206270f5fea80ab7c2ad4ae1/Ratio.py) file we created to simplify functions and formulas, we calculated the sharpe ratios on the `all_coins_df` dataframe. 
Sharpe ratios are used to analyze excess return per unit of risk. 


<img width="830" alt="Screen Shot 2022-04-14 at 6 09 50 PM" src="https://user-images.githubusercontent.com/99091066/163484367-076ce358-f247-491f-930d-c1e9877fe692.png">

 > Descending Order: XRP, Tron, Ethereum, Cronos, Binance, Polymath, Solana, and Fantom.

Generally, a higher sharpe ratio indicates a higher return given the level of risk that was taken. By this definition, XRP indicates a higher investment return per unit of risk compared to its counterparties. Tron also has a very high sharpe ratio at 45.183.

Based on the findings of the Sharpe ratio alone, it is fair to say that XRP generally has a higher risk adjusted performance compared to the other tokens.

Comparing to the benchmark, Solana and Fantom fall short while the other six tokens are outperforming.

### Beta & Rolling Beta

We calculated and plotted the 30 day rolling beta for each token, using 730 trading days. A higher beta indicates a riskier asset. Based on the graph below, it is is evident that Ethereum is the riskiest token as it experiences several spikes over the 2 year period, the highest point being in early 2021. Around this time, Ethereum reached an all time high and the price appreciated by 135% from December 2020 to January 2021 [Source](https://investorplace.com/2021/01/find-other-ways-to-invest-in-cryptocurrencies-than-ethereum/) .

The rapid increase in prices would cause uncertainty in the markets and fears that the bubble would eventually burst. 


<img width="832" alt="Screen Shot 2022-04-14 at 6 37 15 PM" src="https://user-images.githubusercontent.com/99091066/163489062-c570ff8a-82ec-49d3-bf75-26d59a1a55cd.png">

The other tokens are relatively steady, hovering around a beta of 0. 

### Monte Carlo Simulation

The Monte Carlo simulation models risk using possible results/simulations. The model would be a helpful tool in evaluation the performance of tokens because it can predict future outcomes.

Given that we have only two years of data, we decided to run the simulation for 30 days. 

 > We used 5% of the date range we used , in other words 5% of 730 days or 36 days. We decided to use 1 whole month.

Using the formulas and functions in [ratio.py](https://github.com/bleachevil/Classwork/blob/f88b8ef9929a5e53206270f5fea80ab7c2ad4ae1/Ratio.py) , we conducted a simulation for each of the eight tokens.

### XRP 
 <img width="821" alt="Screen Shot 2022-04-16 at 11 41 37 AM" src="https://user-images.githubusercontent.com/99091066/163681490-d3125f4f-671a-4279-8fc1-bf361919be47.png">
 
 For an initial investment of $125, we can say with 95% confidence that it will be valued between $31.89 to $250.37 in the next month.
 In other words, an investment in XRP has the potential to double the initial investment.
 
 ### Solana 
 
<img width="825" alt="Screen Shot 2022-04-16 at 11 41 52 AM" src="https://user-images.githubusercontent.com/99091066/163681497-7faa745c-0c86-4157-b922-aba3b37529e2.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between $10.744 to $332.24 in the next month. The range is fairly high, making this investment risky.

#### Tron

<img width="821" alt="Screen Shot 2022-04-16 at 11 42 04 AM" src="https://user-images.githubusercontent.com/99091066/163681506-882fb829-5d2a-4701-9ea7-787f611eb9ac.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between $55.79 and $218.30 in the next month. The range is modest, with the lower bound still being less than half of the initial investment.

### Polymath


<img width="820" alt="Screen Shot 2022-04-16 at 11 42 39 AM" src="https://user-images.githubusercontent.com/99091066/163681535-d607419d-83c1-456f-af23-654e6198223c.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between $7.13 and $303.35 in the next month. The range is large and the investment can oscillate between high and low. 

### Fantom

<img width="820" alt="Screen Shot 2022-04-16 at 11 42 58 AM" src="https://user-images.githubusercontent.com/99091066/163681542-9735e912-fc13-4180-9e39-3a35383be2f6.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between -$45.38 to $425.80 in the next month. There is a possibilty of losing your entire investment with Fantom, or earning almost triple the initial investment. This would be a consideribly risky investment.

### Ethereum

<img width="824" alt="Screen Shot 2022-04-16 at 11 43 20 AM" src="https://user-images.githubusercontent.com/99091066/163681557-1007678d-1de5-4ccf-b52b-5334a2c6af85.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between $66.644 and $225.82 in the next month. The range is fairly modest and the lower bound is more than half of the initial investment.

#### Cronos

<img width="821" alt="Screen Shot 2022-04-16 at 11 43 32 AM" src="https://user-images.githubusercontent.com/99091066/163681561-bbd7dfff-2d19-4a55-944e-a1aab72ebb78.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between $43.32 and $246.11 in the next month. Cronos' range is not large enough to raise concern about risk. The upper bound is decent.

#### Binance


<img width="822" alt="Screen Shot 2022-04-16 at 11 43 50 AM" src="https://user-images.githubusercontent.com/99091066/163681577-c7f38473-65af-45e0-b8c7-366c8087ab32.png">

For an initial investment of $125, we can say with 95% confidence that it will be valued between $46.56 and $255.77 in the next month.
This investment is safe since the range is not large.




