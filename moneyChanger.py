''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec05.py

constraints: You may not use os.system( "pause" ).

assumtions: The user will not trick or give us bogus input.
E.g.: when asked for a number between 1 and 10 they won't type 125 or hello or something that is not an int within the requested range.
'''


from __future__ import print_function


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
    leftOvers = round(leftOvers, 2)
    pennies = int(leftOvers/0.01)
    leftOvers = leftOvers - (pennies*0.01)
    
    if dollarCoins == 1:
        print("%i" %(dollarCoins) + ''' dollar coin ''')
    elif dollarCoins > 1:
        print("%i" %(dollarCoins) + ''' dollar coins ''')
    if quarters == 1:
        print("%i" %(quarters) + ''' quarter ''')
    elif quarters > 1:
        print("%i" %(quarters) + ''' quarters ''')
    if dimes == 1:
        print("%i" %(dimes) + ''' dime ''')
    elif dimes > 1:
        print("%i" %(dimes) + ''' dimes ''')
    if nickels == 1:
        print("%i" %(nickels) + ''' nickel ''')
    elif nickels > 1:
        print("%i" %(nickels) + ''' nickels ''')
    if pennies == 1:
        print("%i" %(pennies) + ''' pennies ''')
    elif pennies > 1:
        print("%i" %(pennies) + ''' pennies ''')


