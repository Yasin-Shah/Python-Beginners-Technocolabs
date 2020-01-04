class Person:
   __name= None
   __age= None
   AVG_AGE=60
   def setData(self,name,age):
      self.__name= name
      self.__age= age
   def getData(self):
      print("Name is ",self.__name," Age is :",self.__age, "Avg- age is ",Person.AVG_AGE)
   
p= Person()
p.setData("ankur",23)
p.getData()

p1= Person()
p1.setData("amit",25)
p1.getData()


p2= Person()
p2.setData("sumit",23)
p2.getData()



