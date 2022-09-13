string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
i=0
emp_list=[]
while i<len(string_list):
    if string_list[i] not in emp_list:
        emp_list.append(string_list[i])
    i+=1
print(emp_list)