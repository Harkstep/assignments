a=2
b=3

##if


##logical operators not equal !

if a== b:
    print('a is equal to b')


    ## if statement on last item

lang= ['Part','Python','PHP','Ruby']
if 'Python' in lang:
        print('Python is found')

      ## else if

if a == b:
    print('a is equal to b')
elif a>b:
    print('a is greater than b')
else:
    print('some other unexpected condition')

   ## chained conditionals
number = 5
distance = 42
if 0 < number < 42 < distance:
    print('num and distance are within range')
else:
    print('num and distance are out of range')

if 0 < number and number <42 and 42 <distance:
    print('num and dist are within range')

## logical AND operator on chained conditionals
if 0 < number and number <42 and 42 < distance:
    print('num and distance are within range')

mylist = [1,2,3,5,7,9]
if mylist:
    print('the list is not empty')

mylist2 = [0,1,2,3]
if not all(mylist2):
    print('not all are true')

mylist2 = [0, 1, 2, 3]
if any(mylist2):
    print('at least one item is true')

## object type
num = 42
txt = '3'

if int(txt) < num:
    print('txt is less than num')

## while
## while loop
#line = None
#while line != 'done':
 #   line = input('Type "done" to complete')
 #   print('<', line, '>')


## while with break
i=1
while i < 8:
    print(i)
    if i == 4:
        break
    i+=1

##while with continue
i=1
while i < 8:
    i+=1
    if i == 4:
        continue
    print(i)

# while with else
i=1
while i < 8:
    i+=1
    print(i)
else:
    print('i is no longer less than 8')

# for loops       page 229 mimeo

fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)

print('')


fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)
    if x == 'orange':
        break

## create list of 5 foods and loop to print each food

foods = ['pie', 'sausage', 'burger', 'pasta', 'pizza' ]
for dinner in foods:
    print(dinner)
    if dinner.startswith('pi'):
        break
        print(dinner)

for x in 'banana':
    print(x)


some_list = ['john','james','peter','paul']
for i in range(0,len(some_list)):
    print(some_list[i],i)                          #last  i - indexes list

print('')

some_list = ['john', 'james', 'peter', 'paul']
for i in range(0, len(some_list)):
    if i == 2:
        break
    print(some_list[i], i)

print('')
print('')
## for range in step
for x in range(2,20,3):
    print(x)
else:
    print('finished')

###same replacing intigers with variables
print('')
start = 2
end = 20
step = 3

for x in range(start,end,step):
    print(x)
else:
    print('finished')