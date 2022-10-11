def is_int(value):
  try:
    int(value)
    return True
  except:
    return False

A = ["9", "3", "9", "3", "9", "7", "9", "2.23"]


my_dict = dict((i, A.count(i)) for i in A)

# print(my_dict)
# print(type(my_dict))


# for x in my_dict:
#     print (my_dict[x])

odd_list = []
for num in my_dict:
    # print(type(num))
    if is_int(num):
        value = my_dict[num]
        num = int(num)
        # print(f"{num}: {value}")
        if (value % 2) != 0:
            # print("The provided number is odd")
            odd_list.append(num)
        
    # if (isinstance(int(num), float)):
    #     print("error")
    # else:
    #     value = my_dict[num]
    #     # print(f"{num}: {value}")
    #     if (value % 2) != 0:
    #         # print("The provided number is odd")
    #         odd_list.append(num)
    

print(odd_list)
        
        