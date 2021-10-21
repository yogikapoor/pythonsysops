from typing import NewType


my_dict={'fruit': 'apple', 'animal': 'fox', 1: 'one', 'two':2}
# print(my_dict)
# print(my_dict['fruit'])
# print(my_dict.get('animal'))
# my_dict.clear()
# print(my_dict)
# my_dict['three']=3
# print(my_dict)
# my_dict['three']=56
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# new_dict=my_dict.copy()
# print(id(new_dict))
# print(id(my_dict))

# my_new_dict={'four': 4}
# my_dict.update(my_new_dict)
# print(my_dict)
# my_dict.pop('fruit')
# print(my_dict)
# my_dict.popitem()
# print(my_dict)

keys_01=['a','e','i','o','u']
new_dict=dict.fromkeys(keys_01)
new_dict['a']='first alpha'
print(new_dict)

my_dict01={}
my_dict01.setdefault('k',45)
print(my_dict01)
#my_dict01={'fruit'}
my_dict01['fruit']='apple'
#print(my_dict01)
my_dict.setdefault('e','orange') # if key is not present then add value as orange for key=fruit
print(my_dict01)




