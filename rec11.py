''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec11.py

Use this as the starting point for rec11

menu driven program

code is set up to handle the
the four menu choice from rec11

there are stubs for the functions you must write

you will complete:

for Part ONE
	startUpFillWordList( )
	saveWords( )
for Part TWO
	makeHTMLfile( )
for Part THREE
    you will rewrite startUpFillWordList( ) to allow
	a user to choose the name of the file to be read
	from initially.
	you will also complete getValidStartupFilename()
	to be used in your rewrite which takes only the two
	allowed extensions: .clrs and .cpstsv    
'''

from __future__ import print_function

from random import *

wordsWordsWordsFileName = 'wordsWordsWords.txt'
wordList = []
wordsWordsWords = open( wordsWordsWordsFileName, 'r+' ) # r+ means read and write

for line in wordsWordsWords:
    wordList.append(line.strip())


def displayAndGetMenuChoice():
    '''Local function.'''
    choice = int(raw_input(
        '''
1. Display current words
2. Add word to current list
3. Remove word from current list
4. Print an HTML version of words in current list (under construction)
5. Save current list and exit

Enter menu choice: '''))
    return choice

def startUpFillWordList( wordList ):
    ''' opens wordsWordsWords.txt and fills list with words from that file
        the words in that file are one per line
		words in the list must not contain any newline character
    '''
    choice = 0
    while choice != 5:
        choice = displayAndGetMenuChoice()
        if choice == 1:
            print('')
            for line in range(len(wordList)):
                print(wordList[line])
        if choice == 2:
            print('')
            word = raw_input('Enter word: ')
            if word not in wordList:
                wordList.append( word )
        if choice == 3:
            print('')
            wordList.remove(raw_input('Remove word: '))
        if choice == 4:
            makeHTML()
        if choice == 5:
            print('')
            saveWords()
            exit


def saveWords():
    ''' Store current word list into the file: wordsWordsWords.TEXT
	    This will destroy the previous version of the file without
		making a backup.
		words are stored one per line.
	Local function.
    '''
    wordsWordsWords = open( 'sampleTEXT.txt' , 'w' ) #wipe sampleTEXT
    wordsWordsWords.write('\n'.join(wordList))
    for word in range(len(wordList)):
        print(wordList[word])
    wordsWordsWords.close()
    return wordList


def makeHTML(): #title, word, color
    ''' makes file: _________.html using words in wordList
        Local function.
    '''
    userHTMLName = raw_input('Enter file name: ') + '.html' 
    userHTML = open( userHTMLName, 'w' ) 
    heading, headingSize = makeHeading()
    colorSize = askColorSize()
    userHTML.writelines('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">')
    userHTML.writelines('\n<html xmlns="http://www.w3.org/1999/xhtml">')
    userHTML.writelines('\n<head>')
    userHTML.writelines('\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    userHTML.writelines('\n<title>' + heading + '</title>')
    userHTML.writelines('\n</head>')
    userHTML.writelines('\n<body>')
    userHTML.writelines('\n</h' + headingSize + '>' + heading + '</h' + headingSize + '>')
    userHTML.writelines('\n<br />')
    for word in range(len(wordList)):
        wordStyle, wordStyleEnd = makeWordStyle()
        color = makeColor( colorsList, colorSize )
        userHTML.writelines('\n<font color="' + color + '">' +  wordStyle + wordList[word] + wordStyleEnd + '</font><br />')
    userHTML.writelines('\n</body>')
    userHTML.writelines('\n</html>')


def makeHeading():
    'local function.'
    heading = raw_input('''Your heading: ''')
    headingSize = raw_input('''What heading size (1-5)?: ''')
    return heading, headingSize


wordStyleList = [ '<B>', '<I>', '<U>', '<B><U>', '<B><I>', '<U><I>', '<B><I><U>' ]
wordStyleEndList = [ '</B>', '</I>', '</U>', '</B></U>', '</B></I>', '</U></I>', '</B></I></U>' ]

def makeWordStyle():
    'local function.'
    wordStyleRandomInt = randint(0, len(wordStyleList)-1)
    wordStyle = wordStyleList[wordStyleRandomInt]
    wordStyleEnd = wordStyleEndList[wordStyleRandomInt]
    return wordStyle, wordStyleEnd

colorsFileName = 'colors.txt'
colorsList = []
colors = open( colorsFileName, 'r+' )
for line in colors:
    colorsList.append(line.strip())
small = int((1/3)*(len(colorsList))) # 30
medium = int((2/3)*(len(colorsList))) # 60
large = int((3/3)*(len(colorsList))) # 90
colorSizeDict = {'small': small, 'medium': medium, 'large': large}


def askColorSize():
    'local function.'
    colorSize = raw_input('''What color size (small, medium, large)?: ''')
    return colorSize


def makeColor( colorsList, colorSize ):
    colorRandomInt = randint(0, len(colorsList)-1)
    color = colorsList[colorRandomInt]
    return color


def main():
    startUpFillWordList( wordList )
    

main()
