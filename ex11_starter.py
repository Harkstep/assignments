#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

hyphens = "-" * len(Belgium)                        # This takes hyphens and prints them for the length
print(hyphens)                                      # of the Belgium string under new 'hyphens' variable

colons = Belgium.replace(",", ":")                   # This replaces all commas in the string with a colon and
print(colons)                                       # saves it into a new variable, 'colon'

fields = Belgium.split(",")                         # This splits the Belgium string anywhere there is a comma
population = int(fields[1]) + int(fields[3])        # This adds section 2 and 4 together (Python counts from 0)
print(population)
