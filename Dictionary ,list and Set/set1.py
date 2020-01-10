# Methods in Set

s={23,45,"Shagun",56.78,None,"False"}
s1={23,45,"Shagun",None}
print("s=",s)
print("s1= ",s1)
print("Union is ",s.union(s1))
print("Intersection is ",s.intersection(s1))
print("Symmetric Diff is ",s.symmetric_difference(s1))
print("Difference ",s.difference(s1))
print("Difference ",s1.difference(s))
print(s1.issubset(s))
print(s1.issuperset(s))


