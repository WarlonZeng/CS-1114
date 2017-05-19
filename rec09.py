''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec09.py

constraints: learning 2 code

assumtions: im coding
'''

from __future__ import print_function



availableFoods = [
                      "milk", "chocolate covered cherries", "apple", "orange", "banana", "corn on the cob", "kampyo sushi", "asparagus", "avacado", "alfalfa", "acorn squash", "almond package", "arugala bunch",
                      "artichoke", "applesauce", "wasabi", "udon noodles", "tunafish can", "apple juice", "avocado sushi", "bruscetta", "bagel", "barley", "bisque", "bluefish", "bread", "broccoli",
                      "buritto", "babaganoosh", "cabbage", "chocolate cake", "red velvet cake", "strawberry short cake", "carrots", "celery", "cheese", "catfish", "chowder", "clams", "coffee", "corn", "crab",
                      "curry", "cereal", "chimichanga", "dumpling", "donut", "egg", "enchilada", "eggroll", "english muffin", "edimame", "eelSushi", "o toro sashimi", "fajita", "falafel", "fondu", "french toast",
                      "french dip", "garlic", "ginger", "gnocchi", "granola", "grape", "green bean", "guacamole", "gumbo", "grits", "graham crackers", "halibut", "honey", "huenos rancheros", "hash browns", "hummus",
                      "chocolate ice cream", "strawberry ice cream", "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya", "kale", "ketchup", "kiwi", "kidney beans pckg", "great northern beans pckg", "lobster",
                      "linguine", "lasagna", "pepperoni pizza", "mushroom pizza", "pancakes", "quesadilla", "quiche", "spinach", "spaghetti", "tater tots", "toast", "waffles", "walnuts", "peanuts", "hazelnuts",
                      "cranberries", "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt", "pepper", "nutmeg", "yucca", "shichimi"
                      ]

def doNotBuy():
    'creates a list of foods to not buy'
    doNotBuyList = []
    print('-- DO NOT BUY LIST --')
    item = raw_input()
    item = item.lower()
    while item != 'finish':
        if item in availableFoods and item not in doNotBuyList:
            doNotBuyList.append(item)
            item.lower()
        elif item not in availableFoods:
            print('Not in list of allowed foods')
            item = raw_input()
            item.lower()
        else:
            print('Continue...')
            item = raw_input()
            item.lower()
    return doNotBuyList


def shopping(doNotBuyList):
    'creates list of foods to buy'
    shoppingList = []
    print('')
    print('-- TO BUY LIST --')
    item = raw_input()
    item = item.lower()
    while item != 'SHOP':
        if item in availableFoods and item not in doNotBuyList:
            print('Continue...')
            shoppingList.append(item)
            item = raw_input()
            item.lower()
        elif item in doNotBuyList:
            print('Cannot buy item')
            item = raw_input()
            item.lower()
        else:
            print('They do not sell it')
            item = raw_input()
            item.lower()
    return shoppingList


def designatedShopper():
    'combination of shopping and doNotBuy functions'
    doNotBuyList = doNotBuy()
    shoppingList = shopping(doNotBuyList)
    print('-- FAMILY SHOPPING LIST--')
    print(shoppingList)
    return shoppingList


def createWholeList(shoppingList):
    'creates the whole list that includes the number of foods'
    itemList = []
    quantList = []
    wholeList = []
    for item in shoppingList:
        if item not in itemList:
            quantList.append(shoppingList.count(item))
            itemList.append(item)
    for item in range(len(quantList)):
        wholeList.append([itemList[item], quantList[item]])
    wholeList.sort()
    return wholeList


def displayList(wholeList):
    'prints display for family shopping list'
    print('-- FAMILY SHOPPING  LIST --')
    print('FOOD        QUANTITY TO BUY')
    print('---------------------------')
    for item in wholeList:
        print('%s' %(item[0]), end='')
        if item[1]>1:
            print('s', end='')
        print('             %i' %(item[1]))


def displayAvailableFoods():
    'prints list of available foods'
    print('-- List of Available Foods --')
    for i in range(len(availableFoods)):
        print(availableFoods[i])
    print('')


def choiceProgram():
    'gets choice number'
    choice = int(raw_input('''1. add a food item to the shopping list
2. create the DS's I-won't-buy list
3. display an alphabetic list of all available foods
4. quit and print shopping list in alphabetical order

Your choice: '''))
    return choice


def main():
    'the main program to shopping list'
    while True:
        choice = int(raw_input('''1. add a food item to the shopping list
2. create the DS's I-won't-buy list
3. display an alphabetic list of all available foods
4. quit and print shopping list in alphabetical order

Your choice: '''))
        if choice == 3:
            displayAvailableFoods()
        if choice == 2:
            doNotBuyList = doNotBuy()
        if choice == 1:
            shoppingList = shopping(doNotBuyList)
        if choice == 4:
            wholeList = createWholeList(shoppingList)
            displayList(wholeList)


main()
