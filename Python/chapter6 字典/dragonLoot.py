def addToInventory(inventory, addedItems):
    for addedItem in addedItems:
        inventory.setdefault(addedItem, 0)
        inventory[addedItem] += 1
    return inventory


def displayInventory(inventory):
    print('Inventory:')
    for k, v in inventory.items():
        print(v, k)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(addToInventory(inv, dragonLoot))
