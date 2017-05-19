#!C:\Python27\python.exe

''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: hard

filename: rec03.py

constraints:
Code must model this process:
Customers walk up to the cashier,
he asks how many cups of coffee,
then how many doughnuts
and then presents the customer with an itemized bill:

assumtions:
This shop sells coffee by the cup,
   but only one flavor of coffee and no milk or sugar added.
This shop sells doughnuts individually,
   but only one flavor of doughnut.

A cup of coffee costs 77 cents.
A doughnut costs 64 cents .
The tax rate is 8.46%
'''

from __future__ import print_function

taxRate = 0.0846
priceCoffee = 0.77
priceDoughnut = 0.64

def title():
    print('''''')
    print( '''/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ''' )
    print( '''THE COFFEE AND DOUGHNUT SHOPPE ''' )
    print( '''\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ''' )
    print('''''')
def buyCoffee(numCoffee):
    '''displays cups of coffee purchased and amount'''
    costCoffee = numCoffee*priceCoffee
    print( str(numCoffee) + ''' cups of coffee: ''' + "$" + str(costCoffee) )
    return costCoffee
def buyDoughnuts(numDoughnut):
    '''displays doughnuts purchased and amount'''
    costDoughnut = numDoughnut*priceDoughnut
    print( '''     ''' + str(numDoughnut) + ''' doughnuts: ''' + "$" + str(costDoughnut) )
    return costDoughnut
def getTaxed(costCoffee, costDoughnut):
    '''displays tax amount'''
    tax = taxRate*(costCoffee + costDoughnut)
    print( '''             tax: ''' + '''$%.2f\n''' %tax )
    return tax
def getDebt(costCoffee, costDoughnut, tax):
    '''displays total amount to be paid by the consumer'''
    amountOwed = (costCoffee + costDoughnut) - tax
    print( '''    ''' + ''' Amount Owed: ''' + '''$%.2f\n''' %amountOwed )
    return amountOwed
def getThankYoued():
    '''displays the Thank You end message'''
    print( '''Thank you for buying local.''' )

def main():
    numCoffee = int(raw_input( "How many cups of coffee?: " ))
    numDoughnut = int(raw_input( "How many doughnuts?: " ))
    title()
    costCoffee = buyCoffee(numCoffee)
    costDoughnut = buyDoughnuts(numDoughnut)
    tax = getTaxed(costCoffee, costDoughnut)
    amountOwed = getDebt(costCoffee, costDoughnut, tax)
    getThankYoued()

if __name__ == '__main__':
    main()
