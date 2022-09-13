a=[1,2,3,4,5,1,2,3]
i=0
b=[]
c=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1
print(len(c))