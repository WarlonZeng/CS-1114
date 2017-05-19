'''

cs1114

Submission: hwk02.py

Programmer: Warlon Zeng
Username: wz634

Program Level Documentation: a program with a main that calls 2 functions after import

What the program does: show bridge sales brochure

Constraints:
Output will go into the black box python uses which can only be written in left-right and then down order.
Use only function calls and/or the print() function to build your bridges.
There is no input in this homework. - but the help() session should be sufficient

Assumptions: 
Recall that you should not do more than you are supposed to - follow the specs.

'''

from bridgeBuilders import *

def showBridgeSalesBrochure():
    ''' prints Bridge Sales Brochure '''
    singleSpanLight()
    singleSpanHeavy()
    doubleSpanLight()
    doubleSpanHeavy()
    
def pauseTheScreen():
    ''' pauses the screen '''
    raw_input(''' press any key to continue ''')

def main( ):
    showBridgeSalesBrochure( )
    pauseTheScreen( )

main()
