'''

cs1114

Submission: hwk02.py

Programmer: Warlon Zeng
Username: wz634

Program Level Documentation: cs1114 module, 4 functions defined with aid of import

What the program does: bridge builder functions

Constraints:
Output will go into the black box python uses which can only be written in left-right and then down order.
Use only function calls and/or the print() function to build your bridges.
There is no input in this homework. - but the help() session should be sufficient

Assumptions: 
Recall that you should not do more than you are supposed to - follow the specs.

'''

from bridgeParts import *

def singleSpanLight():
    ''' prints Single Span, Light Roadway Bridge '''
    print(''' Single Span, Light Roadway Bridge:\n ''')
    print(singleSpanLightRoadwayLayer())
    print(singleSpanSupportLayer())
    print(singleSpanSupportLayer())
    print(singleSpanSupportLayer())
    print('''''')

def singleSpanHeavy():
    ''' prints Single Span, Heavy Roadway Bridge '''
    print(''' Single Span, Heavy Roadway Bridge:\n ''')
    print(singleSpanHeavyRoadwayLayer())
    print(singleSpanSupportLayer())
    print(singleSpanSupportLayer())
    print(singleSpanSupportLayer())
    print('''''')

def doubleSpanLight():
    ''' prints Double Span, Light Roadway Bridge '''
    print(''' Double Span, Light Roadway Bridge:\n ''')
    print(doubleSpanLightRoadwayLayer())
    print(doubleSpanSupportLayer())
    print(doubleSpanSupportLayer())
    print(doubleSpanSupportLayer())
    print('''''')

def doubleSpanHeavy():
    ''' prints Double Span, Heavy Roadway Bridge '''
    print(''' Double Span, Heavy Roadway Bridge:\n ''')
    print(doubleSpanHeavyRoadwayLayer())
    print(doubleSpanSupportLayer())
    print(doubleSpanSupportLayer())
    print(doubleSpanSupportLayer())
    print('''''')


