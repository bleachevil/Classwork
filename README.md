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

# THE TEAM 

Amira Ali | Jeff Zhang | Nadeem Hassan 

# Tools & Resoures 

## SOFTWARE & TECHNOLOGIES USED 


 <img width="269" alt="Screen Shot 2022-04-14 at 4 13 59 PM" src="https://user-images.githubusercontent.com/99091066/163468356-ae335e88-997a-4ee4-ae0b-e929787c7230.png">

  > Python, Jupyter Notebook, Coingecko API, Plotly for visualization purposes. 


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


<img width="743" alt="Screen Shot 2022-04-14 at 4 33 58 PM" src="https://user-images.githubusercontent.com/99091066/163470971-5f9315aa-e3be-468b-9fcc-43c42cc7cc2f.png">

The prices, market cap, and volume data for each token was then converted to a CSV file and pushed to github for cleaning & analysis. This can be found in the Data folder.

The Prices, Market Cap, and Volume dataframes were all combined into one dataframe.

<img width="1111" alt="Screen Shot 2022-04-14 at 4 46 46 PM" src="https://user-images.githubusercontent.com/99091066/163472580-70ce2d28-a546-4494-9dd2-c98134ce47ae.png">

<img width="1111" alt="Screen Shot 2022-04-14 at 4 48 42 PM" src="https://user-images.githubusercontent.com/99091066/163472799-4c85d117-e413-471e-b0a3-16af85ba90bd.png">

<img width="1090" alt="Screen Shot 2022-04-14 at 4 52 49 PM" src="https://user-images.githubusercontent.com/99091066/163473323-2620788e-accc-481e-aa75-8c6912b50e04.png">

<img width="1103" alt="Screen Shot 2022-04-14 at 4 53 17 PM" src="https://user-images.githubusercontent.com/99091066/163473372-78593ee6-7167-46c8-8378-2d288fb67028.png">

  > We concatenated the data together and dropped null values. The combined dataframes were renamed as `all_coins_df`, `all_vol_df` , `all_MC_df`


# ANALYSIS

In order to compare the tokens, we constructed a balanced ETF to use as a benchmark. 
To do this, we used an arbitrary investment amount `$1000` and divided the investment amount equally amongst the tokens to get `125` per token. We then used `125` and divided this value by the closing prices for each token.

<img width="280" alt="Screen Shot 2022-04-14 at 5 54 58 PM" src="https://user-images.githubusercontent.com/99091066/163482911-f4f5bafb-ad56-4945-9350-b0154f765a80.png">

For the first data point, April 11th, all tokens have an equal $125. Then depending on the fluctuation in token prices, the balanced ETF either increases or decreases according to the sum of the values. 

<img width="724" alt="Screen Shot 2022-04-14 at 5 59 29 PM" src="https://user-images.githubusercontent.com/99091066/163483337-2b340d9e-4f3a-4dab-af23-824512350bd9.png">

The balanced ETF column was combined with the `all_coins_df` dataframe.

<img width="625" alt="Screen Shot 2022-04-14 at 5 59 53 PM" src="https://user-images.githubusercontent.com/99091066/163483384-391d7ae3-16cd-41d2-a656-c53f427450b4.png">



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
















