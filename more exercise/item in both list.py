list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
a=[]
i=0
while i<len(list2):
    if list2[i] in list1:
        a.append(list2[i])
        a.sort()
    i+=1
print(a)
    