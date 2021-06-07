print('*' * 38)
print('''\
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
''')

print('''Appetizers
----------
Wings
Cookies
Spring Rolls
''')

print('''Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
''')

print('''Desserts
--------
Ice Cream
Cake
Pie
''')

print('''Drinks
------
Coffee
Tea
Unicorn Tears
''')
print('*' * 35)
print('** What would you like to order? **')
print('*' * 35)

user_order = {}

def addItem(order):
    
    print(order)
    if order == "quit":
        print(f"Thanks! Come again {user_order}")
        quit()
    elif order in user_order:
        user_order[order] = user_order[order] +1
        print(f"** 1 order of " + order + "have been added to your meal **")
        upSell()
    else:
        user_order[order] = 1
        print(f"{user_order[order]} order of {order} has been added to your order")
        upSell()

def upSell():
    userItem = input("Need something else? > ")
    addItem(userItem)

def quit():
    exit

userItem = input("> ")
addItem(userItem)
