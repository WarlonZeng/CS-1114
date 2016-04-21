''' 
Programmer: Warlon Zeng

Username: wz634

Program Level Documentation: phD

filename: rec05.py

constraints: You may not use os.system( "pause" ).

assumtions: The user will not trick or give us bogus input.
E.g.: when asked for a number between 1 and 10 they won't type 125 or hello or something that is not an int within the requested range.
'''


from __future__ import print_function

from random import randint

def heading():
    print(''' -------------------------------------------- ''')
    print(''' |     Welcome to the snakeStamp Machine!     | ''')
    print(''' | We dispense only 74, 32 and 6 cent stamps. | ''')
    print(''' | We give only coins in change - (no bills). | ''')
    print('''  -------------------------------------------- ''')

def names():
    firstName = raw_input('''What is your first name? ''')
    lastName = raw_input('''What is your last name?''')
    name = firstName + lastName

centStamp74Price = .74
centStamp32Price = .32
centStamp6Price = .06
    
def stamps():
    centStamp74 = int(raw_input('''How many 74 cent stamps would you like? '''))
    return centStamp74
    centStamp32 = int(raw_input('''How many 32 cent stamps would you like? '''))
    return centStamp32
    centStamp6 = int(raw_input('''How many 6 cent stamps would you like? '''))
    return centStamp6
    stampNum = centStamp74 + centStamp32 + centStamp6
    stampNum = str(stampNum)
    return stampNum
    
    total = centStamp74 * centStamp74Price + centStamp32 * centStamp32Price + centStamp6 * centStamp6Price
    total = str(total)
    print('''The price of your ''' + stampNum + ''' stamps is $''' + total)
    dollarsGive = int(raw_input('''How many dollars will you be giving us?''' ))
    print('''Thank you. Just a moment please...''')

    print('''Thanks ''' + name + ''', your change is: ''')

    change = dollarsGive - total
    return change

def thankYou():
    print('''---=======================================---''')
    print('''--- Thank you for using our stamp machine ---''')
    print('''---=======================================---''')

def prize():
    print('''CONGRATULATIONS ''' + firstName + '''!''')
    print('''''')
    print('''You have been chosen to help us evaluate our machine. ''')
    print('''''')
    raw_input('''For helping you will have a chance to win a prize. Please rate our machine by entering a number between 1 and 10,
    with 10 being really great and 1 being horrible: ''')
    
    if rating == randint(1,1000):
        print('''You win $50!!!''')
    elif rating == 2 or 4 or 7 or dollarsGive >= 17.25 and dollarsGive <= 58.42:
        print('''You win $2.33!!!''')
    elif dollarsGive > 1.37:
        print('''You win 37 cents!!!''')
    else:
        print('''You win 3 cents!!!''')
    print('''Thank you for using our stamp machine. ''')

