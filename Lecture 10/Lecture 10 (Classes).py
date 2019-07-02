
# construtor
################################################

# you cannot define multiple constructors

class MyClass:
   def __init__(self):
      self.value=123
#   def __init__(self,thing):
#      self.value=thing
   def set(self,value):
      self.value=value
   def display(self):
      print(self.value)

y=MyClass()
y.display()
y.set(4)
y.display()

# one constructor
################################################

class MyClass:
   def __init__(self,thing=0):
      self.value=thing
   def set(self,value):
      self.value=value
   def display(self):
      print(self.value)

y=MyClass()
y.display()
y.set(4)
y.display()
y.value

################################################
################################################

# static variable
################################################

class C:
   counter = 0
   def __init__(self):
      self.counter += 1
   def show(self):
      print(self.counter)

x = C()
x.show()
y = C()
y.show()

################################################

class C:
   counter = 0
   def __init__(self):
      C.counter += 1
   def show(self):
      print(C.counter)

x = C()
x.show()
y = C()
y.show()

################################################
################################################

################################################

class C:
   counter = 0
   def __init__(self):
      C.counter += 1
   def __del__(self):
      C.counter -= 1

x = C(); print("Number of instances: : " + str(C.counter))
y = C(); print("Number of instances: : " + str(C.counter))
del x; print("Number of instances: : " + str(C.counter))
del y; print("Number of instances: : " + str(C.counter))


################################################
################################################

# inheritance
################################################

class A:
   def __init__(self, data=0):
      self.data = data
   def display(self):
      print (self.data)

class B(A):
   def square(self):
      self.data = self.data * self.data

o = B(5)
o.square()
o.display()

################################################
################################################


# Multiple Inheritance
################################################

class A:
   def A(self):
      print("I am A")

class B:
   def A(self):
      print("I am a")
   def B(self):
      print("I am B")

class C(B,A):
   def C(self):
      print("I am C")

c=C()
c.A()
c.B()
c.C()

################################################
################################################
