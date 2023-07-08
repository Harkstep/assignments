# Create a text file called 'pelican.txt'

with open('pelican.txt', 'w') as file:              # The 'w' opens file as a 'write', As there is no pelican.txt file
    file.write('Pelican:\n')                      # it will create a new one. It will also write over any existing
                                                    # file of the same name.

with open('pelican.txt', 'a') as file:                 # The 'a' appends to the file without deleting existing text.
    file.write('A wonderful bird is the pelican,\n')   # This line states what to write to the file.
                                                              # This is the same principle, In this case I have solely
with open('pelican.txt', 'a') as file:                        # been using 'with open' this statement auto closes the
    file.write('His bill holds more than his belican,\n')     # file so it's ready to work on if you forget to close it.

lines = ['He can take in his beak,\n','Enough food for a week,\n',"But i'm damned if I see how the helican.\n"]
# This is just a regular list, here though \n has been added to tell the file to add each item to a new line.

with open('pelican.txt','a') as file:                  # This opens the file again with an append 'a' file,
    file.writelines(lines)                             # 'writelines' takes all the lines in a list and adds them to
                                                       # the text file

with open('pelican.txt', 'r') as file:                 # This read 'r' function opens the file as read only
    contents = file.read()                             # This creates a variable to capture the content. If this were
    print(contents)                                    # were not used and you try to just print the file itself you
                                                       # will instead slurp the file details.
