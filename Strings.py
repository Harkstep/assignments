## Basic single and Multi strings

somstring = "some string"

somstring1 = """
first line
Some multine strings
Third line
"""

print(somstring)
print(somstring1)

## String Character Sequence Position
print(somstring1[0])
print(somstring1[1])



## String length
print(len(somstring))


## Loop over a string
for x in "sky":
    print(x)

    print('')


## Some string methods
number = 3
Astring = '3'

print(number + int(Astring))    # string needs converted to integer to run with intiger


## string to Upper and lower
print(somstring.upper())
print(somstring.lower())


## full name seperated by commas printed in upper and lower

full_name = 'stephen,harkins'
print(full_name.upper())
print(full_name.lower())
print(len(full_name))


#### String replace
names = 'John, Doe'
print(names.replace('John','Jane'))
print(names)

print('')

### Search a string
print(names.find('Doe'))

print('Doe' in names)        # Returns True statement if found

print('')
print('')

print('x' in names)               # returns False


##Slicing - Substring  -- Start index to Endindex -1
print(names[0:4])

## Slice / get a substring from start to a position
print(names[:4])

## Slice / get a substring from a position to the end
print(names[5:])

## Strip or remove whitespace from a string
names2 = '                         john,Doe          '
print(names2)
print(names2.strip())

## Romeove trailing white space
print(names.rstrip())
## Removing leading white space
print(names.lstrip())


# Concatenate stings
firstname = 'John'
lastname = 'Doe'
fullname = firstname + " " + lastname + " " + "test"
print(fullname)

age = 20
message = "I am"+ str(age)+"years old"
print(message)

##format

message1 = "I am {} years old"
print(message.format((age)))

message2 = "I am {} years old, and I like {}"
print(message2.format(age, 'Python'))


# ends and starts with
message3 = 'Welcome to Python'
print(message3.startswith('Welcome'))
print(message3.endswith('Python'))


print(message3.startswith('e'))
print(message3.endswith('o'))

##Split a string into a list
message4 = "Welcome to Python's Coolness"
print(message4.split())

message4 = "Welcome to Python's Coolness"
splitlist = message4.split()


# iterate over the new list
for x in splitlist:
    print(x)


##Escape Characters

message5 = "Hello world, it is \"sunny\" today"
print(message5)

message6 = "Hello world, It is \nsunny today"
print(message6)


# Making string
# extrect vowels
# reverse string
# split string
groupstring = 'lou serene callum stephen'
vowels = 'aeiou'
count = 0

for number in groupstring:
    if number in vowels:
        count += 1

print("Number of vowels in the string:", count)

reversed = groupstring[::-1]
print(reversed)

list = groupstring.split()
print(list)
