class First:
	def __init__(self,a,b):
		self.a=a
		self.b=b
    def add(a,b):
    	x=self.a+self.b
		return x
    def sub(a,b):
		y=self.a-self.b
		return y	
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
#c=int(input("enter the value of c: "))	
f=First(a,b)
print(f.add())
print(f.sub())
	
