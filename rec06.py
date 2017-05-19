''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec06.py

constraints: learning 2 code

assumtions: im coding
'''

from __future__ import print_function

from random import *

from sys import *

valid = 0

def getSingleChar():
    '''get CHARACTER from user'''
    singleChar = raw_input('Enter single character: ')
    return singleChar

        
def checkValid(singleChar):
    '''this function also checks for valid interval because the game automatically assumes invalidation for user input not in interval
    i.e if user: 1 not equal to randint 4 valid 2,3,4,5,6 the input is invalid anyway
    also checks for length due to hardwired nature of the game
    i.e 12 cannot be 2 
    exits upon valid'''
    if singleChar == '#' or '%' or '@':
        valid = 1
    middleDigit = randint(2,7)
    for i in range(1,3):
        upperMiddleValue = str(middleDigit + i)
        lowerMiddleValue = str(middleDigit - i)
        if singleChar == upperMiddleValue:
            valid = 1
        elif singleChar == lowerMiddleValue:
            valid = 1
        else:
            valid = 0
    if valid != 1:
        print('''Sorry, try again''')
    if valid == 1:
        exit()

def inputValidationLoops():
    '''get character input, check validity'''
    singleChar = getSingleChar()
    checkValid(singleChar)
    

def main():
    '''runs the guessing game'''
    while True:
        inputValidationLoops()

main()
