fruits = ['Apples',
'Apricots',
'Avocados'
'Bananas',
'Bing Cherry',
'Blueberries',
'Boysenberries',
'Cantaloupe',
'Cherries',
'Clementine',
'Crab apples',
'Cucumbers',
'Damson plum',
'Dates',
'Dewberries',
'Dinosaur Eggs',
'Dragon Fruit',
'Eggfruit',
'Elderberry',
'Entawak',
'Evergreen Huckleberry',
'Farkleberry',
'Fig',
'Finger Lime',
'Gooseberries',
'Grapefruit',
'Guava',
'Hackberry'
'Honeycrisp Apples',
'Imbe',
'Indonesian Lime',
'Jackfruit',
'Jambolan',
'Java Apple',
'Kaffir Lime',
'Kiwi',
'Kumquat'
'Lime (Lemon)',
'Longan',
'Loquat',
'Lychee',
'Mango',
'Melon',
'Mulberry',
'Nashi Pear',
'Navel Orange',
'Nectarine',
'Ogeechee Limes',
'Olive',
'Oranges',
'Oval Kumquat',
'Papaya',
'Paw Paw',
'Peach',
'Pineapple',
'Pomegranate',
'Prickly Pear',
'Quararibea cordata',
'Queen Anne Cherry',
'Quince',
'Rambutan',
'Raspberries',
'Star Fruit',
'Strawberries',
'Sugar Baby Watermelon',
'Tamarind',
'Tangerine',
'Tart Cherries',
'Tomato',
'Ugni',
'Uniq Fruit',
'Vanilla Bean',
'Velvet Pink Banana',
'Voavanga',
'Watermelon',
'White Mulberry',
'Wolfberry',
'Xango Mangosteen',
'Xigua','Ximenia caffra fruit','Yangmei','Yellow Passion Fruit','Yunnan Hackberry','Zig Zag Vine fruit','Zinfandel Grapes','Zucchini']





def getHash(string):
    temp=0

    s1=string[3:]
    s2=string[:3]
    for char in s1:
        temp+=ord(char)

    for char in s2:
        temp+=ord(char) 

    # new_string=string[0].lower()+string[1:].upper()
    # for char in new_string:
    #     temp+=ord(char)

    return temp


def hash_function(hash,size):
    index=int(hash%(size))
    return index

fruit_dict=[0]*1000


def insert(dict):
    collison=0
    for element in fruits:
        hash=getHash(element)

        index=hash_function(hash,len(fruit_dict))
        if dict[index] == 0:
            dict[index]=element
        else:
            collison+=1
    print('Total Collision at',collison)



insert(fruit_dict)
