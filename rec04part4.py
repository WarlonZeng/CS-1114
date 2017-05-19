''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec04.py

constraints: none

assumtions: 1 pesos = 0.066 usd
'''
'''

coffee shop
demo program in labs
reduced from coffee and doughnut problem

'''

PRICE_PER_CUP = 1.25 # in US$

from rec04part2 import printAsCoins

def getNumCoffeeCups():
    ''' returns user's coffee order quantity '''

    cups = int( raw_input( "How many cups, Snakey? " ) )
    # might want to make sure it's a valid number here
    return cups

def calcOwed( numberCups ):
    ''' returns calculated amount owed '''

    return numberCups * PRICE_PER_CUP

def showBill( cups, owed ):
    ''' presents bill nicely '''

    print "You owe $" + str( owed ) + "\n" + \
          "for your " + str( cups ) + " cups(s)"

def main():
    qntCups = getNumCoffeeCups()
    owed = calcOwed( qntCups )
    showBill( qntCups, owed )
    printAsCoins( owed )

main()
