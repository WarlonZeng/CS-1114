'''

cs1114

Submission: hwk01.py

Programmer: Warlon Zeng
Username: wz634

Program Level Documentation: cs1114 module

What the program does: Create tools for text flag designer to design text flags

Special Tricks: strings can be used as parameters by char = 'string' for functions defined below.

Constraints: Output will go into the black box python uses which can only be written in left-right and then down order.
You cannot use anything that has not been covered up until now in labs or lectures - just function def-ing and calling and local variables, and paramters and global constants and using the print and raw_input functions.
(Wow! that's a lot!)

Assumptions: 
-(They code in python also so "on screen" means in the UI that you are already familiar with.)
-no raw_input used because it is not deemed necessary and module is not executable
-functions are called and "stitched"

'''


from __future__ import print_function


def caret():
    ''' Prints the caret
    Moves cursor to new line '''
    print( '''^''' )


def topSubUnit( char ):
    ''' Use char = 'Your character' for NaN
    Example: topSubUnit(char = 'OOOOO')
    Makes beginning sub unit string
    Leaves cursor on line '''
    topSubUnit = str( char )
    topSubUnit = '''|''' + topSubUnit
    print( topSubUnit, end='' )
    return topSubUnit


def midSubUnit( char ):
    '''Use char = 'Your character' for NaN
    Example: midSubUnit(char = 'OOOOO')
    Makes middle sub unit string
    Leaves cursor on line'''
    midSubUnit = str( char )
    print( midSubUnit, end='' )
    return midSubUnit


def botSubUnit( char ):
    ''' Use char = 'Your character' for NaN
    Example: botSubUnit(char = 'XOXOX')
    Makes last sub unit string
    Moves cursor to new line '''
    botSubUnit = str( char )
    botSubUnit = '''''' + botSubUnit
    print( botSubUnit )
    return botSubUnit


def oneCharLine( char ):
    ''' Use char = 'Your character' for NaN
    Example: oneCharLine(char = 'X')
    Makes 15 of the same character
    Moves cursor to new line '''
    oneCharLine = str( char )*15
    oneCharLine = '''|''' + oneCharLine
    print( oneCharLine )
    return oneCharLine


def endFlag():
    ''' Prints the two poles at the end
    Moves cursor to new line '''
    print( '''|''' )
    print( '''|''' )
