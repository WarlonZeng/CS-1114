#!C:\Python27\python.exe

''' 
cs1114 

Submission: hw07

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

make and display dictionary of donations

Assume:

sentinel

'''

from __future__ import print_function

#10.00 + 8.99 + 15.01 is NOT 1034.01


dicty = {}
keyVal = 'initial'

sentinels = ['Botty', 'Roboat', 'Borot']

def updateValueAtKey(dicty, keyVal, floatToAdd):
    ''' Takes a dictionary of str -> float key/value pairs.
        Assume that this kind of dictionary will be passed in.
        Adds the floatToAdd value to the float value in the
        dictionary at keyVal.
        E.g.: if dicty['john'] is  12.22 and the call:
        updateValueAtKey( dicty, 'john', 100 ) is made, 
        then, after the call, dicty['john'] is 112.22
        If the key is not in the dictionary, inserts the
        the key/value pair: keyVal -> floatToAdd
        into the dictionary. '''
    if keyVal in dicty.keys():
        dicty[keyVal] += floatToAdd
    else:
        dicty[keyVal] = floatToAdd
    return dicty


def getDonAmtFromStd(dicty, keyVal):
    'get donations'
    donateIterations = int(raw_input('How many donations? '))
    for donate in range(donateIterations):
        floatToAdd = float(raw_input())
        updateValueAtKey(dicty, keyVal, floatToAdd)
    return dicty


def printStudentDonationData( dictyKeys ):
    'prints data'
    print('')
    print('')
    print('''Everyone's donations: ''')
    print('')
    for index in range(len(dictyKeys)): # for some reason dictyKeys gives me a dictionary and a list.. if you do type(dictyKeys)
        name = dictyKeys[index]
        print(name, '$' + str(dicty[name]))

    
def sortAlphabetically(dicty):
    'sorts alphabetically; dictykeys is list and dictionary...'
    dictyKeys = dicty.keys()
    dictyKeys.sort()
    return dictyKeys


def welcomeMSG():
    'welcome msg'
    print('Welcome Snakenicker')


def getName():
    'get the name'
    keyVal = raw_input('''What is your name?
''')
    return keyVal


def donationProgram(keyVal, dicty):
    'run the program'
    while keyVal not in sentinels:
        welcomeMSG()
        keyVal = getName()
        if keyVal not in sentinels:
            dicty = getDonAmtFromStd(dicty, keyVal)
            print('')


def main(dicty):
    'the program'
    donationProgram(keyVal, dicty)
    dictyKeys = sortAlphabetically(dicty)
    printStudentDonationData(dictyKeys)


main(dicty)
