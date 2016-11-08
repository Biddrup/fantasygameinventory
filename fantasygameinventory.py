# inventory.py
#This is take a stuff from you
stuff = {}

#This will help you to find out items and
#Update the database
while True:
    #This will take input from user
    print('Enter an item: (blank to quit)')
    #This is not case sensetive
    name = input()

    #If input '', then loop will be terminated
    if name == '':
        break

    #This will keep the input as uppercase
    newname = name.upper()
    
    #This will check the name in databse or not 
    if newname in stuff:
        #If the input in databse, this will print
        print('Value for ' + newname + ' is ' + stuff[newname])

    else:
        print('I do not have the information for ' + newname)
        #This will take info under that name
        print('What is the value')
        items = input()
        stuff[newname] = items
        #And, databse is updated now
        print('Stuff database updated')


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
