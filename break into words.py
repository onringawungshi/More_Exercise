# sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# def break_into_words(user):
#     list_of_words=user.split()
#     return list_of_words
# print(break_into_words(input("enter sentence:")))

def numbers_less_than_twenty(list):
    counter = 0
    emp_list=[]
    while counter < len(num_list):
        if  num_list[counter]> 20:
            pass
        else:
            emp_list.append(num_list[counter])
        counter+=1

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", emp_list)