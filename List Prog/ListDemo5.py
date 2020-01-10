# Remove
l1=[24,67,56,45,89,23,4,6,8]
print(l1)
l1.remove(67)
print(l1)
print(l1.pop()) # Return+remove last element
print(l1)

print(l1.pop(4))
print(l1)

del l1[0]
print(l1)

del l1[1:3]
print(l1)

#del l1
l1.clear()
print(l1)
