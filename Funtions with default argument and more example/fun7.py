# VarArgs

def add(*a):
	sum=0
	for i in a:
		sum= sum+i
	print("Sum is ",sum)

add()
add(1,2,3)
add(1,2)
add(1,3,4,5,7,8,9)
add(6,7,9,9,9,0,6,6,5,4)
