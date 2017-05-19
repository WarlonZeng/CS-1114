def didHeWin(sameLength, userName):
    if sameLength == 1:
        heWon = 1
    elif userName == '''Python''':
        heWon = 1
    else:
        heWon = 0
    if heWon == 1:
        print('''YAG!''')
        print('''You won a marble!''')
    else:
        print('''YAG!''')
    print('''You were off by ''' + str(len(userWordPhrase) - len(userName))
    return heWon
