import random

class Portfolio:
    audit_log = [] # audit log list

    def __init__(self, cash = 0.0):
        self.cash = cash
        # dictonary for invest gruops
        self.invest_dict = {"Stock": {}, "Mutual Fund": {}, "Bond": {}} # Investment dictionary
        log_history = "Portfolio is createdwith cash of $" + str(self.cash)
        self.addLog(log_history) 
    
    # print(Portfoilo)
    def __repr__(self): # Returns a string as a representation of the object
        print("-------Details about Portfolio---------\nCash: $" + str(self.cash))
        print("\nYour Assets: ")    
        for type, info in self.invest_dict.items():
            print(type.capitalize())
# !!How can get only the value of each Assets without <__main__.xx>?
            for x in info:
                print(x, info[x])
        return("\n")
    
    # add log function for history 
    def addLog(self, log_history):
        Portfolio.audit_log.append(log_history) 

    def history(self):
        print("-----------Portfoil History------------")
        print('\n'.join(map(str, Portfolio.audit_log)))


    def addCash(self, amount):
        self.cash += amount # cash add about amount cash
        log_history = "$" + str(amount) + " added, Current Cash balance: $ " + str(self.cash)
        self.addLog(log_history)


    def withdrawCash(self, amount):
        afterWithdraw = self.cash - amount
        log_history = "$" + str(amount) + " withdrawen, Current Cash balance: $ " + str(afterWithdraw)
        self.addLog(log_history)
        # amount is which I want to take away
        if self.cash < amount:
            print("You don't have enough cash for buying. Please charge more")
        else:
            self.cash -= amount

# buy Invest for Stock, Mutual Funds, Bonds
    def buyInvest(self, amount, invest):
        payForBuy = amount * invest.price

        if self.cash < payForBuy:
            print("You don't have enough money to buy")    
            return None
        self.withdrawCash(payForBuy)

        if invest in self.invest_dict[invest.getName()]:
            self.invest_dict[invest.getName()][invest] += amount
        else:
            self.invest_dict[invest.getName()][invest] = amount
        log_history = "You bought %s of %s which called %s\n" % (amount, invest.getName(), invest.name)
        self.addLog(log_history)

    def buyStock(self, amount, invest):
        self.buyInvest(amount, invest)

    # same buyInvest for Bond and Fund
    buyBond = buyMutualFund = buyInvest 

#    def sellInvest(self, amount, invest):
#        if self.invest_dict[invest.getName()][invest] < amount:  # check that there is enough to sell
#            print("The portfolio does not contain enough of %s %s" % (invest.name, invest.getName()))
#        else:
#            self.invest_dict[invest.getName()][invest] -= amount
#            if self.invest_dict[invest.getName()][invest] == 0:  # check if sold all of it - delete key if so
#                del self.invest_dict[invest.getName()][invest]
#            self.addCash(amount * invest.priceForSell())  #call function asset.SellPrice to calculate price of asset
#            log_history = "You sold %s of %s named %s\n" % (amount, invest.getName(), invest.name)
#            self.addLog(log_history)
            
#    def sellStock(self, amount, invest):
#        self.sellInvest(amount, invest)
        
#    sellBond = sellMutualFund = sellInvest

# the order is different in compared to buy categories
    def sellMutualFund(self, invest, amount):
        if invest in self.invest_dict['Mutual Fund']:  # check that it's in the portfolio
            earning = 100 * (random.uniform(0.9, 1.2)) * amount 
            self.addCash(amount * earning) #Cash added
            self.invest_dict['Mutual Fund'][invest] -= amount #Number of owned shares decreased
            log_history = str(amount) + " shares of " + invest + " sold for $" + str(earning) + ", Cash Balance: $" + str(
                self.cash)
            self.addLog(log_history) #Entry to Audit Log
            return "Mutual Fund sold"
        else:
            print("Error")

    def sellStock(self, invest, amount):
        if invest in self.invest_dict['Stock']:  # check that it's in the portfolio
            earning = random.uniform(0.5, 1.5) * amount 
            self.cash += earning #Cash added
            self.invest_dict['Stock'][invest] -= amount #Number of owned shares decreased
            log_history = str(amount) + " shares of " + invest + " sold for $" + str(earning) + ", Cash Balance: $" + str(
                self.cash)
            self.addLog(log_history) #Entry to Audit Log
            return "Mutual Fund sold"
        else:
            print("Error")

# Parent for childclass (Stock, MutualFund, Bonds)
class Invest:
    def __init__(self, price, name):
        self.price = price
        self.name = name


class Stock(Invest):
    def __init__(self, price, name):
        super().__init__(price, name) # inheritance from Invest

    def getName(self):
        return "Stock"


class MutualFund(Invest):
    def __init__(self, name):
        super().__init__(self, name) # inheritance from Invest
        self.price = 1.0

    def getName(self): 
        return "Mutual Fund"



# Third type of investments for BONUS
class Bond(Invest):
    def __init__(self, price, name):
        super().__init__(price, name) # inheritance from Invest

    def getName(self): 
        return "Bond"


portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio

portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50


portfolio.addCash(1000)  # Adds cash to the portfolio

# ---------------------------------BONUS------------------------------
print("BONUS POINTS for Bonds") 
# Creates bond b with value 20, symbol "KOC"
b = Bond(20, "KOC")  
portfolio.buyBond(4, b)  # Buys bond b

portfolio.history()
print(portfolio)  # Prints portfolio
