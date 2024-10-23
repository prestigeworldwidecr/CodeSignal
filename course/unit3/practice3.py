'''

Alright, Space Voyager! Here's a real-world situation: You're a data analyst for a universal retail conglomerate managing two clothing stores, let's call them Space Threads and Galaxy Garments. You have two lists named inventory1 and inventory2 representing the clothing items from these stores. Now, your prime mission is to figure out the clothes that are exclusive to each store. Note that the letter casing is not important, so items like "t-shirt" and "T-Shirt" are considered the same. Return all exclusive clothes sorted in alphabetical order.

Keep in mind that we're dealing with text data here. The length of these lists can range from as few as no items to as many as a star cluster. There is zero room for error, kid. Now, get to it!

Hint: To compare items, ignoring the casing, convert all elements to uppercase.

'''

def list_toUppercase(l) :
# {

    for i in range(len(l)) :
    # {
        l[i] = l[i].upper()
    # }

    return l

# }

def exclusive_products(inventory1, inventory2) :
# {
    # implement this
    
    r1 = set()
    r2 = set()
    tmp = [None, None]
    result = [None, None]
    tmp[0] = list_toUppercase(inventory1)
    tmp[1] = list_toUppercase(inventory2)

    r1 = set(tmp[0])
    r2 = set(tmp[1])

    r3 = r1 - r2
    r4 = r2 - r1

    # print('!', r1, r2, r3, r4)
    result[0] = sorted(r3)
    result[1] = sorted(r4)

    return (result[0], result[1])
# }

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

'''

********
BONEYARD
********

.upper()
inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])

# return list_toUppercase(inventory1)

'''