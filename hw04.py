''' 
cs1114 

Submission: hw04

Programmer: warlon zeng
Username: wz634

Purpose of program, assumptions, constraints:

Define a function that takes two lists and returns a list of those elements that both have in common.

The ordering of the returned list must match the order of the first parameter.

Make sure to not have duplicates in the returned list.

Assume:

two lists

'''


from __future__ import print_function


def removeDups(commonElements):
    ''' Removes duplicates from a list '''
    commonElementsNoDups = []
    for i in range(len(commonElements)):
        if commonElements[i] not in commonElementsNoDups:
            commonElementsNoDups.append(commonElements[i])
    commonElements = commonElementsNoDups
    return commonElements


def getCommonElements(list1, list2):
    ''' gets a common list of elements from two lists
        no duplicates
        works on any sized elements (i.e. 5 vs 9)
        code optimized for two lists only
    '''
    commonElements = []
    for i in range(len(list1)):
            if list1[i] in list2:
                commonElements.append(list1[i])
    commonElements = removeDups(commonElements)
    return commonElements

