def factorial(user):
    i=1
    factorial=1
    while i<=user:
        factorial=factorial*i
        i+=1
    return factorial
print(factorial(int(input("enter number:"))))