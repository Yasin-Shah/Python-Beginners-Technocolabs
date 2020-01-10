# Default Arg

def add(x,y,a=0,b=0):
	print("Sum is ",(a+b))
	return a+b

print(add(10,30))
print(add(10,30,89,90))
print(add(10,30,89))
