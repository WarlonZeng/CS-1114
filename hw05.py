''' 
cs1114 

Submission: hw05

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

Define a function that takes two lists and returns a list of those elements that both have in common.

The ordering of the returned list must match the order of the first parameter.

Make sure to not have duplicates in the returned list.

Assume:

two lists

two lists return in one list (one return)

duplicates allowed
'''


from __future__ import print_function


def getCommonPosition(list1, list2):
    ''' gets a common list of elements from two lists
        duplicates allowed
        works on any sized elements (i.e. 5 vs 9)
        code optimized for two lists only
    '''
    firstList = []
    secondList = []
    commonPositionList = []
    for i in range(len(list1)):
        if list1[i] in list2:
            firstList.append(i)
    commonPositionList.append(firstList)
    for i in range(len(list2)):
        if list2[i] in list1:
            secondList.append(i)
    commonPositionList.append(secondList)
    return commonPositionList

