# Nested Dictonary
p= {'name':"Nikku", 'age':21, 'address':'indore',
'marks':{'maths':78,'phy':67,'chem':45}}

print("Dict is ",p)
"""
for data in p.items(): 
 print(data)

"""

for k,v in p.items():
 if type(v)==type({}):
  for k1,v1 in v.items():
   print(k1,"---",v1)
 else:
  print(k,">>",v)
