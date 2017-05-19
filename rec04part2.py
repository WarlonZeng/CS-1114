''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec04.py

constraints: none

assumtions: 1 pesos = 0.066 usd
'''

from __future__ import print_function

def printAsUSDollars(USD):
    dollarOrUSD = int(raw_input('''Enter 0 to display dollar sign or enter 1 to display USD: ''')) 
    '''Given an amount of money (a floating point value),
    this function prettyprints the amount in $9999.99 form,
    rounding up to the next whole penny. '''
    USD = round(USD, 2)
    USD = str(USD)
    print('''$''' + USD) if (dollarOrUSD == 0) else print('''USD ''' + USD)

def convertPesosToUSDollars(PESOS):
    dollarOrUSD = int(raw_input('''Enter 0 to display dollar sign or enter 1 to display USD: '''))
    USDConv = 0.066
    USD = PESOS*USDConv
    wholeUSD = int(USD)
    leftOvers = (USD - wholeUSD)
    wholeUSD = str(wholeUSD)
    leftOvers = str(leftOvers)
    print('''$''' + wholeUSD + leftOvers) if dollarOrUSD == 0 else print('''USD ''' + wholeUSD + leftOvers)

def printAsCoins(USD):
    USD = round(USD, 2)
    dollarCoins = int(USD)
    leftOvers = (USD - dollarCoins)
    quarters = int(leftOvers/0.25)
    leftOvers = leftOvers - (quarters*0.25)
    dimes = int(leftOvers/0.10)
    leftOvers = leftOvers - (dimes*0.10)
    nickels = int(leftOvers/0.05)
    leftOvers = leftOvers - (nickels*0.05)
    pennies = int(leftOvers/0.01)
    leftOvers = leftOvers - (pennies*0.01)
    dollarCoins = str(dollarCoins)
    quarters = str(quarters)
    dimes = str(dimes)
    nickels = str(nickels)
    pennies = str(pennies)
    print('''Dollar Coins: ''' + dollarCoins)
    print('''Quarters: ''' + quarters)
    print('''Dimes: ''' + dimes)
    print('''Nickels: ''' + nickels)
    print('''Pennies: ''' + pennies)
    
def quantityOfCoins(USD):
    USD = round(USD, 2)
    dollarCoins = int(USD)
    leftOvers = (USD - dollarCoins)
    quarters = int(leftOvers/0.25)
    leftOvers = leftOvers - (quarters*0.25)
    dimes = int(leftOvers/0.10)
    leftOvers = leftOvers - (dimes*0.10)
    nickels = int(leftOvers/0.05)
    leftOvers = leftOvers - (nickels*0.05)
    pennies = int(leftOvers/0.01)
    leftOvers = leftOvers - (pennies*0.01)
    totalCoins = dollarCoins + quarters + dimes + nickels + pennies
    totalCoins = str(totalCoins)
    print('''Total Coins: ''' + totalCoins)


    
