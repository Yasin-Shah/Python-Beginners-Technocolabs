# If Condition
a=int(input("Enter value of a\n"))
b=int(input("Enter value of b\n"))
c=int(input("Enter value of c\n"))
d=int(input("Enter value of d\n"))
if a>b and a>c and a>d:
 print("a is greater",a)
elif b>c and b>d:
 print("b is greater",b)
elif c>d:
 print("c is greater",c)
else:
  print("d is greater",d)
