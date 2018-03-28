from portfolio import PortfolioGenerator
import pandas as pd
import numpy as np

class SampleStrategy(PortfolioGenerator):

    def __init__(self):
        pass

    def build_signal(self, stock_features):
        #return some combination of our signals by z-scoring...

    def momentum(self, stock_features):
        return stock_features.groupby(['ticker'])['returns'].mean()
        
    def book_to_price(self, stock_features):
        #pull price to book data, reverse it (1 / pb = bp), and organize by highest to lowest
        
    def industry(self, stock_features):
        #fetch industry data for a specific stock
        
    #others to come...

# Test out performance by running 'python sample_strategy.py'
if __name__ == "__main__":
    portfolio = SampleStrategy()
    sharpe = portfolio.simulate_portfolio()
    print("*** Strategy Sharpe is {} ***".format(sharpe))
