''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec08.py

constraints: learning 2 code

assumtions: im coding
'''

from __future__ import print_function

from rec05 import *

def drawStar():
    ''' draws a star on the screen '''
    starSize = int(raw_input('''enter the star size: '''))
    for i in range(1,starSize):
        raw_input()


def powerList(starting, ending, expo=2):
    '''makes a list of power values '''
    powerList = [i**expo for i in range(starting, (ending+1))]
    return powerList

    
def hypenList(numList):
    '''makes a number of hypens based on the list'''
    lenOfList = len(numList)
    for i in range(0, lenOfList):
        numInIndex = numList[i]
        for j in range(0, numInIndex):
            print('-', end='')
        print(' (' + str(numInIndex) + ')', end='')
        print('')


def statReport():
    '''write "Manager" at "press any key to continue" to end the loop'''
    numOfCustomers = 0
    largestPurchase = 0
    smallestPurchase = 9999
    moneyAccumulated = 0
    avgPurchase = 0
    purchased32CentStampEqual = 0
    key = 0
    while key != 'Manager':
        print('')
        (dollarsGive, change, total, centStamp74, centStamp32, centStamp6, key) = stampMachine()
        numOfCustomers += 1
        if total >= largestPurchase:
            largestPurchase = total
        if total <= smallestPurchase:
            smallestPurchase = total
        if (centStamp32 == centStamp74) or (centStamp32 == centStamp6):
            purchased32CentStampEqual += 1
    moneyAccumulated += total
    avgPurchase = (moneyAccumulated / numOfCustomers)
    purchased32CentStampEqual = float(purchased32CentStampEqual)
    numOfCustomers = float(numOfCustomers)
    percentPurchased32CentStampEqual = ((purchased32CentStampEqual / numOfCustomers) * 100)
    purchased32CentStampEqual = int(purchased32CentStampEqual)
    numOfCustomers = int(numOfCustomers)
    print('')
    print('~~~Status Report~~~')
    print('Number of customers: ' + str(numOfCustomers))
    print('Largest purchase: ' + '$' + str(largestPurchase))
    print('Smallest purchase: ' + '$' + str(smallestPurchase))
    print('Average purchase: ' + '$' + str(avgPurchase))
    print('% of customers who purchased the same number of 32 cent as either of the other stamps: ' + str(percentPurchased32CentStampEqual) + '%')
    print('')

statReport()
