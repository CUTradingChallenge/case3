from portfolio import PortfolioGenerator
import pandas as pd
import numpy as np

class SampleStrategy(PortfolioGenerator):

    def __init__(self):
        pass

    def build_signal(self, stock_features):
        return self.momentum(stock_features)

    def momentum(self, stock_features):
        #return(stock_features.groupby(['ticker'])['returns'].mean())

        pbaverage = stock_features.groupby(['ticker'], as_index=False)['pb'].mean()
        #print(pbaverage)
        pbsorted = pbaverage.sort_values(['pb'])

        firstten = pbsorted[:10]
        #print (firstten)

        isinstock=stock_features[stock_features.ticker.isin(firstten.ticker)]
        #print(isinstock)


        stock_features.loc[:,'weight'] = 0
        isinstock.loc[:,'weight']= 1

        appendeddata=isinstock.append(stock_features)
        #print (appendeddata)
        finaldata= appendeddata.drop_duplicates(subset='ticker', keep='first')
        #print (finaldata)
        finalsorted=finaldata.sort_values(by=['ticker','weight'])
        #print(finalsorted)
        output = finaldata.loc[:].set_index('ticker')['weight']
        #print (output)
        #print(filteredtdf)

        #print(stock_features)
        #return stock_features
        #print(stock_features)
        #print(tickerarray)

        return output

# Test out performance by running 'python sample_strategy.py
if __name__ == "__main__":
    portfolio = SampleStrategy()
    sharpe = portfolio.simulate_portfolio()
    print("*** Strategy Sharpe is {} ***".format(sharpe))
