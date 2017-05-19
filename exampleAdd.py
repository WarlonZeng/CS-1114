from __future__ import print_function

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
    
quantityOfCoins(1.25)

