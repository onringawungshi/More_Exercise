user=int(input("enter no. of students:"))
i=0
sum=0
while i<user:
    user1=int(input("enter your expense:"))
    sum=sum+user1
    i+=1
if sum<50000:
    print("less budget")
else:
    print("ok")