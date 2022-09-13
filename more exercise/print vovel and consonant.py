user=input("enter name:")
b,c=[],[]
for i in user:
    if i in("a","e","i","o","u","A","E","I","O","U"):
        b.append(i)
    else:
        c.append(i)
print(b,"vowel list")
print(c,"consonant list")