

# String with an item
someString = 'Norwegian Blue'


# Collection with items
SomeStringList = ['Banana', 'apples','guava','oranges']
numberList = [3,5,7,9,1]

# Arithmatic Operations on list
print('min:',min(numberList))
print('min:',min(numberList))
print('min:',min(numberList))

print('')
print('')

## Access individual items using their indexes
print(numberList[0])
print(numberList[2])


# Length of a list
print('Length of a list is',len(numberList))

# Return a range of items from a list, Start index included, up to and not including next indexes
print(numberList[1:3])

# items from the start of a list to a position
print(numberList[:3])
# from position 3 to the end
print(numberList[3:])

# Change Items
numberList[0]= 90
numberList[3] = [50,50]

print(numberList)
# add items to a list

fruitlist = []
fruitlist += ['mangoes','pineapple']
print(fruitlist)

# Remove Items
fruitlist.remove('mangoes')
print(fruitlist)

#iterate a loop over a list
for fruit in fruitlist:
    print(fruit)


#
count = fruitlist.count('pineapple')
print('pineapple occur', count, ' times')

#find the index of an item
fruitlist.index('pineapple')

# find the index of a non existing item
# fruitlist.index('cars')

print('')
print('')
fruitlist.append('pear') # added so below list had more than one item
#sort list items
fruitlist.sort()
print(fruitlist)
fruitlist.sort(reverse=True)
print(fruitlist)


# Dictionary

mydict = {'Australia':'Canberra', 'Eire':'Dublin','france':'Paris'}
print(mydict['Australia'])

country = 'Iceland'
mydict[country] = 'Reykjavik'

print(mydict['Iceland'])

print('')
print('')

mydict2 = {'UK':['London','Wigan','Manchester'],'US':['Miami','New York','Boston']}
print(mydict2['UK'][2])

mydict2['FR'] = ['Paris','Lyon','Bordeaux']
print(mydict2['FR'][2])

# for item in mydict2:
#     print(mydict2(item))

# find longest fruit and length of it
fruits = [ 'apples', 'pear', 'orange', 'pinapple']
print((fruits))

maxfruit = max(fruits)
lenmaxfruit = len(maxfruit)

print(maxfruit,'is', lenmaxfruit, ' characters long')

#----------------------------------------Alternate way

Peter: fruits = ["apple", "banana",  "watermelon", "pineapple"]
longest_fruit = ""
max_characters = 0
for fruit in fruits:
    if len(fruit) > max_characters:
        longest_fruit = fruit
        max_characters = len(fruit)
print("Fruit with the longest name:", longest_fruit)
print("Number of characters:", max_characters)


# page 285

#open in read mode

infile=open('newtextfile.txt', 'r')
infile.close
print(infile.read())


print('')

#readline
infile2 = open('newtextfile','r')
line= infile2.readlines()
print(line)
infile2.close()



