#!C:\Python27\python.exe

'''

cs1114

Submission: hwk03.py

Programmer: Warlon Zeng
Username: wz634

Program Level Documentation:
Writing a program for playing the Hit && Match game.
a program (that is not a module) that includes looping and subparts


Constraints:
Notice the singular/plural outputs - you must not use a branching statement for this.
Do not use lists (or tuples which won't work) for storing the user's three guesses or the house' three digits.
- We have not gotten to using these sequences in detail yet so the graders will think you are getting code from someone else.
You must follow the posted style guidelines.
Your code must be "double-clickable" as usual.
There are no modules to write for this homework.
You are not allowed to use any looping statements other than the one we gave you in main.


Assumptions:
You can assume the player will type numeric input when you ask for it.
Assume the user, when asked for single digits, will give only single digit inputs.
Recall that assumptions of this sort must be documented in the program level docstrings


!!!!!! sys.exit(17) traceback thingy: !!!!!!!
i have no idea why python doesn't show the traceback error. i literally read
all there is on sys.exit on the website.
i could make a raw_input('''''') to pause the screen (for users double-clicking)
but i do not want to include anything that are not in the specs.
also professor gallgaher said if there's something off about sys.exit,
he told me to mention it on the program saying he said something about it.

'''



from random import *



import sys



def getHouse():
    ''' A function that randomly chooses the house' three digits
    No two digits should be the same.
    For this homework, when any pair of digits is the same,
    tell the user that the game has malfunctioned and end the program reporting an error value to the OS/IDLE.
    This error should be the value 17
    bonus!!!: insert code "print left, mid, right" to find out numbers =) '''
    left = randint(0,9)
    mid = randint(0,9)
    right = randint(0,9)
    houseLeft = left
    houseMid = mid
    houseRight = right
    dup = noDupsPlz(left, mid, right)
    if dup == 1:
        print('''We are sorry but the game has malfunctioned. ''')
        print('''Ending... ''')
        sys.exit(17)
    return (houseLeft, houseMid, houseRight)



def noDupsPlz(left, mid, right):
    ''' A function that tests is any pair of digits is the same in a trio of passed in digits'''
    if left == mid:
        dup = 1
    elif left == right:
        dup = 1
    elif mid == right:
        dup = 1
    else:
        dup = 0
    return dup



def getUserInput():
    ''' A function that allows a player to choose their three guesses for digits.
    No two guesses should be the same but if they are,
    tell the user that this is considered an invalid try and end processing for this user.
    The infinite loop will take over and go to the next user.
    bonus!!!: insert code "print left, mid, right" to find out numbers =) '''
    left = int(raw_input('''Enter digit for left position: '''))
    mid = int(raw_input('''Enter digit for mid position: '''))
    right = int(raw_input('''Enter digit for right position: '''))
    userLeft = left
    userMid = mid
    userRight = right
    dup = noDupsPlz(left, mid, right)
    if dup == 1:
        print('''Sorry, that is an invalid try. ''')
        endTurn = 1
    else:
        endTurn = 0
    return (userLeft, userMid, userRight, endTurn)



def getHit(houseLeft, houseMid, houseRight, userLeft, userMid, userRight):
    ''' A function that determines and returns the number of hits based on the player's three guesses and the house' three digits '''
    hit = 0
    if houseLeft == userLeft:
        hit += 1
    if houseMid == userMid:
        hit += 1
    if houseRight == userRight:
        hit += 1
    return hit



def getMatch(houseLeft, houseMid, houseRight, userLeft, userMid, userRight):
    ''' A function that determines and returns the number of matches based on the player's three guesses and the house' three digits '''
    match = 0
    if houseLeft == userMid:
        match += 1
    if houseLeft == userRight:
        match += 1
    if houseMid == userRight:
        match += 1
    return match



def displayHitAndMatch(hit, match):
    if hit == 1:
        print hit, str('''hit ''')
    if hit >1 or hit == 0:
        print hit, str('''hits ''')
    if match == 1:
        print match, str('''match ''')
    if match >1 or match == 0:
        print match, str('''matches ''')



def playOneHitAndMatchGame():
    ''' the Hit && Match game
    skip display for hit and matches if user enters any common digits '''
    print('''Welcome to the Hit && Match Game ''')
    raw_input('''hit any key to start playing... ''')
    print('''''')
    (houseLeft, houseMid, houseRight) = getHouse()
    (userLeft, userMid, userRight, endTurn) = getUserInput()
    hit = getHit(houseLeft, houseMid, houseRight, userLeft, userMid, userRight)
    match = getMatch(houseLeft, houseMid, houseRight, userLeft, userMid, userRight)
    if endTurn != 1:
        displayHitAndMatch(hit, match)
    print('''Come back and play again sometime ''')
    print('''''')



def main():
    ''' runs the Hit && Match game loop '''
    while True:
        playOneHitAndMatchGame()



main()
