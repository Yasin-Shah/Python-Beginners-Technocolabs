# Single level
class A:
   """This is Parent Class"""
   def m1(self):
      print("Class A")

class B(A):
   """This is Child Class """
   pass
   

b= B()
b.m1()
print(B.__base__)
print(A.__base__)
