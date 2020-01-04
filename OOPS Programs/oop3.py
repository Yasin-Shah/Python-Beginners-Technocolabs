class Test:
   """This is First OOP class"""
   
   def show(self):
      print("Hello Show")
      

print(Test.__doc__)
print(Test.__base__)
print(Test.__module__)
print(Test.__name__)
print(int.__module__)
print(int.__base__)

t= Test()
print(t)

