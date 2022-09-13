big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
i=0
while i<len(big_list):
    j=0
    while j<len(big_list[i]):
        print(big_list[i][j])
        j+=1
    i+=1