
# Tuples
ls=(1,3,5,7)
# ls[0]=2
print (ls)
print(ls[0])

print ("--------------------------------------------------")

# List
ls=[1,3,5,7]
ls[0]=2
print (ls)
print(ls[0])

print ("--------------------------------------------------")

# List syntax
ls = []
print (ls)
ls.append(5)
print (ls)

print ("--------------------------------------------------")

ls2 = [1,3,5,7]
print (ls2)
print (ls2[0])
ls2.append('hi')
print (ls2)
print (len(ls2))

print ("--------------------------------------------------")

import random
print (random.randrange(0,10))

print("----------------------------------------------------------")

# Dictionary
student={}
print (student)
student['name']='mhd kabbani'
student['year']=4
student['courses']=['PL','SWE']
student[40]='id'
student[3.4]='AGPA'
student[(3,5)]='coordinates'
print(student)
print(student['name'])
print(student.get('year'))
print(student.keys())
print(student.values())



