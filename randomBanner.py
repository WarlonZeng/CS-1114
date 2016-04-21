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

from random import randint

def top():
    ''' Prints top
    Moves cursor to new line '''
    print( '/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ' )


def firstMid():
    ''' Makes first mid line
    Leaves cursor on line '''
    lineSeg = randint(4,5)
    if lineSeg == 4:
        firstSeg = chr(randint(97,122)) * randint(4,6)
        secondSeg = chr(randint(97,122)) * randint(4,6)
        thirdSeg = chr(randint(97,122)) * randint(4,6)
        fourthSeg = chr(randint(97,122)) * randint(4,6)
        fifthSeg = ''''''
    elif lineSeg == 5:
        firstSeg = chr(randint(97,122)) * randint(4,6)
        secondSeg = chr(randint(97,122)) * randint(4,6)
        thirdSeg = chr(randint(97,122)) * randint(4,6)
        fourthSeg = chr(randint(97,122)) * randint(4,6)
        fifthSeg = chr(randint(97,122)) * randint(4,6)
    if len(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg) < 30:
        trailNum = 30 - len(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg)
        trail = str( "<" ) * trailNum
    print(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg + trail)

    
def secondMid():
    ''' Makes first mid line
    Leaves cursor on line '''
    lineSeg = randint(4,5)
    if lineSeg == 4:
        firstSeg = chr(randint(97,122)) * randint(4,6)
        secondSeg = chr(randint(97,122)) * randint(4,6)
        thirdSeg = chr(randint(97,122)) * randint(4,6)
        fourthSeg = chr(randint(97,122)) * randint(4,6)
        fifthSeg = ''''''
    elif lineSeg == 5:
        firstSeg = chr(randint(97,122)) * randint(4,6)
        secondSeg = chr(randint(97,122)) * randint(4,6)
        thirdSeg = chr(randint(97,122)) * randint(4,6)
        fourthSeg = chr(randint(97,122)) * randint(4,6)
        fifthSeg = chr(randint(97,122)) * randint(4,6)
    if len(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg) < 30:
        trailNum = 30 - len(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg)
        trail = str( "<" ) * trailNum
    print(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg + trail)

def thirdMid():
    ''' Makes first mid line
    Leaves cursor on line '''
    lineSeg = randint(4,5)
    if lineSeg == 4:
        firstSeg = chr(randint(97,122)) * randint(4,6)
        secondSeg = chr(randint(97,122)) * randint(4,6)
        thirdSeg = chr(randint(97,122)) * randint(4,6)
        fourthSeg = chr(randint(97,122)) * randint(4,6)
        fifthSeg = ''''''
    elif lineSeg == 5:
        firstSeg = chr(randint(97,122)) * randint(4,6)
        secondSeg = chr(randint(97,122)) * randint(4,6)
        thirdSeg = chr(randint(97,122)) * randint(4,6)
        fourthSeg = chr(randint(97,122)) * randint(4,6)
        fifthSeg = chr(randint(97,122)) * randint(4,6)
    if len(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg) < 30:
        trailNum = 30 - len(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg)
        trail = str( "<" ) * trailNum
    print(firstSeg + secondSeg + thirdSeg + fourthSeg + fifthSeg + trail)


def bot():
    ''' Prints bot
    Moves cursor to new line '''
    print( '''\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/''' )
    
def randomBanner():
    top()
    firstMid()
    secondMid()
    thirdMid()
    bot()
