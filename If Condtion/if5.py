day=input("Enter day\n")
print(type(day))
amount=int(input("Enter amount\n"))
if day=="sunday":
 if amount>=20000:
  print("Go for Shopping")
 else:
  print("watch moive at home")
else:
 print("go to work")
