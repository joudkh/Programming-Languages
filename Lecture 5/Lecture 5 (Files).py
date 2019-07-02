f=open ('in.txt', 'r')
nameList=f.read()
names=nameList.split('\n')
names.sort()

target = open('out.txt', 'w')
for name in names:
   print(name)
   target.write(name)
   target.write('\n')
target.close()
f.close()
