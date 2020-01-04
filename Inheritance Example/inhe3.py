# Multiple
class A:
   """This is Parent Class"""
   def m1(self):
      print("Parent Class A")

class B:
   """This is Parent Class """
   def m1(self):
      print("Parent Class B")


class C(B,A):
   """This is Child Class """
   pass
c= C()
c.m1()
print(C.__base__)
print(B.__base__)
print(A.__base__)
