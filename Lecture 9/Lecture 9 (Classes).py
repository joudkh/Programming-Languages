# in python every thing is an object
# "hello".upper()
# list.append('a')
# dict.keys()

# simple class
################################################

# classes can be defined anywhere
# all methods and variables are public

class MyClass:
   def set(self,value):
      self.value=value
   def display(self):
      print(self.value)

y=MyClass()
y.set(4)
y.display()
print(y.value)

################################################
################################################


# construtor
################################################

class MyClass:
   def __init__(self):
      self.value=123
   def set(self,value):
      self.value=value
   def display(self):
      print(self.value)

y=MyClass()
y.display()
y.set(4)
y.display()


################################################
################################################


# private variables
################################################

# Python has no concept of private variables,
# but leading underscores are used to indicate variables
# that must not be accessed from outside the class.


class Hello:
   def __init__(self):
      self.x=0
      self.y=0
      self._value="Hello World!!!"
   def show(self):
      print(self._value)
   def setX(self,x):
      self.x=x
   def setY(self,y):
      self.y=y
   def sum(self):
      return self.x+self.y

instance=Hello()
instance.setX(5)
instance.setY(7)
instance.show()
print(instance.sum())

################################################
################################################
