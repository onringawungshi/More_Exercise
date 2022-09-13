user=input("enter name and age:")
b=[]
for i in user:
    b.append(i)
for j in b:
    if j>="a" and j<="z":
        print(type(j))
    elif j>="A" and j<="Z":
        print(type(j))
    else:
        v=int(j)
        print(type(v))