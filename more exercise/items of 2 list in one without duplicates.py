list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
emp_list=[]
while i<len(list1):
    if list1[i] not in emp_list:
        emp_list.append(list1[i])
    j=0
    while j<len(list2):
        if list2[j] not in emp_list:
            emp_list.append(list2[j])
        j+=1
    i+=1
emp_list.sort()
print(emp_list)
    