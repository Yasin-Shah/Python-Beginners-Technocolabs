# Hierarchial
class A:
   """This is Parent Class"""
   def m1(self):
      print("Parent Class A")
      
class B(A):
   """This is Child Class """
   def m1(self):
      print("Child Class B")
      
class C(A):
   """This is Child Class """
   def m1(self):
      print("Child Class C")
   def m2(self):
      print("Child Class C m2")
      
c= C()
c.m1()
c.m2()
b= B()
b.m1()
a= A()
a.m1()
a.m2()

print(C.__base__)
print(B.__base__)
print(A.__base__)
