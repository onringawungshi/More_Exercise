def que():
    a={"a":10,"b":20,"c":16,"d":4,"e":17}
    u=input("enter key")
    u1=int(input("enter value to substract"))
    for j in a:
        if j==u:
            if a[j]>u1:
                b=a[j]-u1
            else:
                b=u1-a[j]
            return b
print(que())