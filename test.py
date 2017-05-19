def getUserFirstWordPhraseNum():
    userFirstName = raw_input('''Your name: ''')
    userWordPhrase = raw_input('''Your phrase: ''')
    userNum = raw_input('''Enter a positive integer: ''')
    return userFirstName, userWordPhrase, userNum


def checkWordPhraseNumLength(userWordPhrase, userNum):
    sameLength = (len(userWordPhrase) == len(userNum))
    return sameLength


def didHeWin(sameLength, userNum, userFirstName):
    if sameLength == 1:
        heWon = 1
    elif userFirstName == '''Python''':
        heWon = 1
    else:
        heWon = 0
    if heWon == 1:
        print('''YAG!''')
        print('''You won a marble!''')
    else:
        print('''YAG!''')
        print('''You were off by ''' + str(abs(len(userNum) - len(userFirstName))))


def main():
    (userFirstName, userWordPhrase, userNum) = getUserFirstWordPhraseNum()
    sameLength = checkWordPhraseNumLength(userWordPhrase, userNum)
    didHeWin(sameLength, userNum, userFirstName)


main()
