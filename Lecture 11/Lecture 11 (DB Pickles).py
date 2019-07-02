# simply by using files (read / write)


# Pickle your data
# Python ships with a standard library called pickle, which can save and load
# almost any Python data object, including lists.

# Once you pickle your data to a file, it is persistent and ready to be read into
# another program at some later date/time:

# Save with dump and restore with load

import pickle

write=open('mydata', 'wb')
pickle.dump("hello", write)
write.close()

read=open('mydata', 'rb')
value = pickle.load(read)
read.close()

print(value)

print("----------------------------------------------------------")

##########################################

import pickle

write=open('mydata', 'wb')
pickle.dump("hello", write)
pickle.dump([1, 2, 'three'], write)
write.close()

read=open('mydata', 'rb')
value1 = pickle.load(read)
value2 = pickle.load(read)
read.close()
print(value1)
print(value2[0])

"""
problems with pickling:
- Pickle files must be accessed in sequential order:
You cannot say "give me the 3rd variable stored in the file"
The solution to this problem is 'shelves'.
"""

