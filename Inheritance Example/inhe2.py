# Multilevel
class A:
   """This is Parent Class"""
   def m1(self):
      print("Class A")

class B(A):
   """This is Child Class """
   def m1(self):
      super().m1()
      print("Class B")


class C(B):
   """This is Child Class """
   def m1(self):
      super().m1()
      print("Class C")


   

c= C()
c.m1()
print(C.__base__)
print(B.__base__)
print(A.__base__)
