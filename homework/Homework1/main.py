nameOfStock = []

nameOfStock = input("which name of stock you want to buy? ")


print(nameOfStock)

class Portfolio:
    cash = []
    def __init__(self, cash=None, stock=None, mutualFunds=None):
        self.cash = cash
        self.stock = stock
        self.mutualFunds = mutualFunds
        
    def addCash(money):
        cash = input("How much money you want to put? ")
        money = float(cash) + float(money)

Portfolio.addCash()
print()

class Stock(Portfolio):
    def __init__(self, price=None, name=None):
        self.price = price
        self.name = name

    def buyStock(self, amount, symbol):
        self.amount = amount
        self.symbol = symbol


s = Stock(20, "HFH")
print(f"you have {s.price} and {s.name}")
print(Stock)

class MutualFunds:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price



# portfolio = Portfolio() #Creates a new portfolio
# portfolio.addCash(300.50) #Adds cash to the portfolio
# s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
# portfolio.buyStock(5, s) #Buys 5 shares of stock s
# mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
# mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
# portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
# portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
# print(portfolio) #Prints portfolio
#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT
# 2 GHT
# portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
# portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
# portfolio.withdrawCash(50) #Removes $50
# portfolio.history() #Prints a list of all transactions
#ordered by time

