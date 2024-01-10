'''
my_list=[]
my_list1=[3,4,5,'python', 'devops',5.6]
print(f"{bool(my_list)}, { bool(my_list1)}") # boolean value if list is empty its False
print(my_list1, type(my_list1))

print(my_list1[3])
print(my_list1[-1])
print(my_list1[3][1])
my_list1[0]=45
print(my_list1)
'''
my_list2=[3,5,2,7,3,8,9,5]
print(my_list2.index(5))
print(my_list2.count(10))
print(my_list2.count(5))
#my_list2.clear()
print(my_list2)
my_new_list=my_list2
my_one_list=my_list2.copy()
print(id(my_new_list), id(my_one_list))

my_list2.append(56) # Adding value at the end 
print(my_list2)
my_list2.insert(1,45) # it will add  value in a given index value
print(my_list2)
my_list2.extend(my_list2)
print(my_list2)
my_list2.remove(5)
print(my_list2)
print(my_list2.pop()) # pop we can use with print coz it will print what value it is removing
my_list2.reverse
print(my_list2)
my_list2.sort
print(my_list2)
my_list2.reverse
print(my_list2)











