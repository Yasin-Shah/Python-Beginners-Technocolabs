s= "a23 Abcd 456 Abc &*"
print(s)
for ch in s:
	if ch.isdigit():
	 continue
	print(ch,end=" ")
