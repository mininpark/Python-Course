import inspect
class Portfolio:
    def __init__(self):
        self.cash = 0
        # dictonary for invest gruops
        self.invests = {"stock": {}, "mutual funds": {}, "bonds": {}}
        

    def addCash(self, cash):
        self.cash += int(cash * 100) / 100.0 


    def withdrawCash(self, cash):
        if self.cash < cash:
            print("You don't have enough cash for buying. Please charge more")
        else:
            self.cash -= int(100 * cash) / 100.0


    def buyStock(self, amount, invest):
        self.buyInvest(int(amount), invest)


    def buyInvest(self, amount, invest):
        if self.cash < amount * invest.price:
            print("You don't have enough cash for buying. Please charge more")
            return None
        self.withdrawCash(amount * invest.price)

        if invest in self.invests:
            # how to check if 
            inspect.isclass(invest) += amount
        else:
            inspect.isclass(invest) = amount

    def buyStock(self, amount, invest):
        self.buyInvest(int(amount), invest)

    def buyMutualFund(self, amount, invest):
        self.buyInvest(int(amount), invest)

    def buyBonds(self, amount, invest):
        self.buyInvest(int(amount), invest)


class Invest(object):
    def __init__(self, price, name):
        self.price = price
        self.name = name
class Stock(Invest):
    def __init__(self, price, name):
        self.price = price
        self.name = name


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

