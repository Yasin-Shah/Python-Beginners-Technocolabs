class Person:
   name= None# class variable
   age= None
   
   def setData(self,name,age):
      self.name= name
      self.age= age
   
p= Person()
p.setData("ankur",23)
print("Name is ",p.name," Age is :",p.age)

p1= Person()
p1.setData("amit",25)
print("Name is ",p1.name," Age is :",p1.age)

p2= Person()
p2.setData("sumit",23)
print("Name is ",p2.name," Age is :",p2.age)


