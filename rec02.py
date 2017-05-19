#!C:\Python27\python.exe

''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: Easy

filename: rec02.py

constraints: none

assumtions: none
'''


def welcome():
    '''displays Welcome'''
    print("Welcome")
def drawBaseLines():
    '''draws the base line'''
    print('''XXXXXXXXX''')
def drawSpace():
    '''draws space upper and lower boxes'''
    print('''X       X''')
def drawMiddle():
    '''draws the middle line'''
    print("X  JOE  X")
def thankYou():
    '''displays welcome'''
    print("Thank You")
def main():
    welcome()
    drawBaseLines()
    drawSpace()
    drawMiddle()
    drawSpace()
    drawBaseLines()
    thankYou()
    import os
    os.system('pause')
if __name__ == '__main__':
    main()
