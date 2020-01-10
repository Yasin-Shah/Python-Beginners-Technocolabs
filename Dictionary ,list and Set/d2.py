# Nested Dictonary
p= {'name':"Nikku", 'age':21, 'address':'indore',
'marks':{'maths':78,'phy':67,'chem':45}}
print("Dict is ",p)

# Get Items

print("Name is: ",p['name'])
print("Age is: ",p['age'])
print("Address is: ",p['address'])
print("Marks is: ",p['marks'])
print("Maths Marks is: ",p['marks']['maths'])
print("Phy Marks is: ",p['marks']['phy'])
print("Chem Marks is: ",p['marks']['chem'])
