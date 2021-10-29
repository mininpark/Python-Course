import random

class Portfolio:
    audit_log = [] # audit log list

    def __init__(self, cash = 0.0):
        self.cash = cash
        # dictonary for invest gruops
        self.invest_dict = {'Stock': dict(), 'Mutual Fund': dict(), 'Bond': dict()} 
        log_history = "Portfolio is initally created with cash of $" + str(self.cash)
        self.addLog(log_history)

    # print(Portfoilo)
    def __repr__(self): # Returns a string as a representation of the object
        print("----------Details about Portfoilo-------------\nCash: $"+ str(self.cash))
	    
        return "Stock: %s \nMutual Fund: %s \nBond: %s" %(self.invest_dict['Stock'], self.invest_dict['Mutual Fund'], self.invest_dict['Bond'])

    # add log function for history 
    def addLog(self, log_history):
        Portfolio.audit_log.append(log_history) 

    def history(self):
        print("-----------Portfoil History------------")
        print('\n'.join(map(str, Portfolio.audit_log)))


    def addCash(self, amount):
        self.cash += amount # cash add about amount cash
        log_history = "$" + str(amount) + " added \t Your Wallet: $ " + str(format(self.cash, ".2f"))
        self.addLog(log_history)


    def withdrawCash(self, amount):
        afterWithdraw = self.cash - amount
        log_history = "$" + str(amount) + " withdrawen \t Your Wallet: $ " + str(format(afterWithdraw, ".2f"))
        self.addLog(log_history)
        # amount is which I want to take away
        if self.cash < amount:
            print("You don't have enough cash for buying. Please charge more")
        else:
            self.cash -= amount

# BUY PART
    def buyStock(self, amount, invest):
        priceToBuy = invest.price * amount 

        self.cash -= priceToBuy 
        if invest.name in self.invest_dict['Stock']: 
            self.invest_dict['Stock'][invest.name] += amount 
        else:  
            self.invest_dict['Stock'][invest.name] = amount 
        log_history = "You bought " + str(amount) + " stocks of " + invest.name + " for $" + str(
                priceToBuy) + "\t" + "Your Wallet: $ " + str(format(self.cash, ".2f")) # float two digits
        self.addLog(log_history)
        return "You bought stock!"

# just change the ID 'Stock', but it would be better if I could shorten with one class name or sth
    def buyMutualFund(self, amount, invest):
        priceToBuy = invest.price * amount 
        self.cash -= priceToBuy 
        if invest.name in self.invest_dict['Mutual Fund']: 
            self.invest_dict['Mutual Fund'][invest.name] += amount 
        else:   #If not owned
            self.invest_dict['Mutual Fund'][invest.name] = amount 
        log_history = "You bought " + str(amount) + " mutual funds of " + invest.name + " for $" + str(
                priceToBuy) + "\t" + "Your Wallet: $ " + str(format(self.cash, ".2f")) 
        self.addLog(log_history) 
        return "You bought Mutual Fund"

# Bonus Part for Bond, as like Fund, just change the name of id with same format
    def buyBond(self, amount, invest):
        priceToBuy = invest.price * amount 
        self.cash -= priceToBuy 

        if invest.name in self.invest_dict['Bond']: 
            self.invest_dict['Bond'][invest.name] += amount
        else:   #If not owned
            self.invest_dict['Bond'][invest.name] = amount 
        log_history = "You bought " + str(amount) + " Bond of " + invest.name + " for $" + str(
                priceToBuy) + "\t" + "Your Wallet: $ " + str(format(self.cash, ".2f"))
        self.addLog(log_history) 
        return "You bought Bond"

# SELL PART (the order is somehow changed by assignment)
    def sellStock(self, symbol, amount):
        priceToSell = int(random.uniform(0.5, 1.5) * amount * 100) / 100.0 
        self.cash += priceToSell 
        self.invest_dict['Stock'][symbol] -= amount 
        log_history = "You sold " + str(amount) + " stocks of " + symbol + " for $" + str(priceToSell) + ", Your Wallet: $" + str(format(self.cash, ".2f"))
        self.addLog(log_history) 
        return "You sold Stock!"

    def sellMutualFund(self, symbol, amount):
        priceToSell = int(random.uniform(0.9, 1.2) * amount * 100) / 100.0 
        self.cash += priceToSell #Cash added
        self.invest_dict['Mutual Fund'][symbol] -=  amount 
        log_history = "You sold " + str(amount) + " mutual funds of " + symbol + " for $" + str(priceToSell) + ", Your Wallet: $" + str(format(self.cash, ".2f"))
        self.addLog(log_history) #Entry to Audit Log
        return "You sold Mutual Fund!"

    def sellBond(self, symbol, amount):
        priceToSell = int(random.uniform(0.4, 1.4) * amount * 100) / 100.0 
        self.cash += priceToSell #Cash added
        self.invest_dict['Bond'][symbol] -=  amount 
        log_history = "You sold " + str(amount) + " bonds of " + symbol + " for $" + str(priceToSell) + ", Your Wallet: $" + str(format(self.cash, ".2f"))
        self.addLog(log_history) #Entry to Audit Log
        return "You sold Bond!"


# Parent for childclass (Stock, MutualFund, Bonds)
class Invest:
    def __init__(self, price, name):
        self.price = price
        self.name = name
class Stock(Invest):
    def __init__(self, price, name):
        super().__init__(price, name) # inheritance from Invest

class MutualFund(Invest):
    def __init__(self, name):
        super().__init__(self, name) # inheritance from Invest
        self.price = 1.0
class Bond(Invest):
    def __init__(self, price, name):
        super().__init__(price, name) # inheritance from Invest


# Assignments
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

# -------------------------BONUS-----------------------------
# Creates bond b with value 20, symbol "KOC"
d = Bond(20, "KOC")  
portfolio.buyBond(4, d)  # Buys bond d
portfolio.history()
print(portfolio)  # Prints portfolio

