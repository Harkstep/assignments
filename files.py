# page 285

#open in read mode

infile=open('newtextfile.txt', 'r')
infile.close
print(infile.read())


print('')

#readline
infile = open('newtextfile.txt','r')
line= infile.readlines()
print(line)

# read the whole line
lines = open('newtextfile.txt').read().splitlines()

## Sefer recommended way to open files
with open('newtextfile.txt','r') as infile:
    for line in infile:
        print(line,end='')



# infile = open('newtextfile.txt','r').read()
# print(infile)



# Writing to file, WILL OVERWRITE ANYTHING IN FILE!!
output = open('newtextfile.txt','w')
output.write('7\n')
output.close()

##Append to a file
output2 = open('newtextfile.txt','a')
output2.write('7\n')

fruits = ['oranges', 'mangoes']
output2.writelines(fruits)

fruits = ['oranges\n', 'mangoes\n']
output2.writelines(fruits)

# for fruit in fruits
#     output2.write(fruit)
#     output2.write('\n')

#varfruit = banana


