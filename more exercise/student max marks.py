marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
def maximum():
    i=0
    emp_list=[]
    while i<len(marks):
        j=0
        m=0
        while j<len(marks[i]):
            if marks[i][j]>m:
                m=marks[i][j]
            j+=1
        i+=1
        print(m)
maximum()
        