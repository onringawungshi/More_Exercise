user1=int(input("enter number:"))
user2=int(input("enter number:"))
user3=int(input("enter number:"))
if user1>user2 and user1>user3:
    print(user1,"max")
elif user2>user1 and user2>user3:
    print(user2,"max")
else:
    print(user3,"max")