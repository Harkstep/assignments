cheese = ['Chedder', 'Stilton', 'Cornish Yarg']     # This is a list
cheese += 'Oke'                                     # 'Oke' is a string, you can not concatenate a string to
print(cheese)                                       # a list, Here it returns 'Oke' as separate entities.

cheese = ['Chedder', 'Stilton', 'Cornish Yarg']
cheese.append('Oke')                              # Using the append function turns the 'Oke' into an element
print(cheese)                                     # Which can be added (appended) to the list.


                                                 # We could add two lists together with + concatenation
cheese.extend(['Brie', 'Blue'])                  # Simply using .extend allows us to add multiple objects to
print(cheese)                                    # the list using only one command

