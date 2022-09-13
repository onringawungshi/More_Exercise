# def harshad(user):
#     x=list(str(user))
#     i,sum,s=0,0,""
#     while i<len(x):
#         sum=sum+int(x[i])
#         s=s+x[i]
#         i+=1
#     if int(s)%sum==0:
#         print("harshad")
#     else:
#         print("not harshad")
# harshad(int(input("enter number:")))

def harshad(user):
    a=user
    i,sum=0,0
    while i<user:
        r=user%10
        user=user//10
        sum=sum+r
        i+=1
    if a%sum==0:
        print("harshad")
    else:
        print("not harshad")
harshad(int(input("enter number:")))