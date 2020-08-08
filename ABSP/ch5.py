stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print('Inventory: ')
    item_total=0
    for k,v in inventory.items():
        print(str(v),k)
        item_total+=v
    print('total number of items: ' +str(item_total))

#displayInventory(stuff)

def addToInventory(inventory,addedItems:list):
#    count = 0
#    for i in addedItems:
#        count+=1
#    print(addedItems)
    for i in addedItems:
#        print(i)
        if i in inventory.keys():
#            print("!!!!!!")
            inventory[i]=inventory[i]+1
        else:
#            print("豬豬")
            inventory[i]=1
#        for k,v in inventory.items():
#            if str(i) == str(k)
#                v+=1
#        inventory[i]=1
#        displayInventory(inventory)

#    print (count)
    return inventory
inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby', 'ruby']
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
