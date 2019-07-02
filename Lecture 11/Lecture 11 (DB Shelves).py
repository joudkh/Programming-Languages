# Shelves let you store and retreive variables in any order using pickling.
# Shelves need a name to get the data. So, it works like a dictionary
# given a name, lookup the data

import shelve

pickles = shelve.open('mydata')
pickles['variety'] = ['sweet', 'hot', 'dill']
pickles['shape'] = ['whole','spear','chip']
pickles.close()

pickles = shelve.open('mydata')
shapes = pickles['shape']
pickles.close()

print (shapes)
