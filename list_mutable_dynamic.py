a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(a)
a[2] = 10
a[-1] = 20
print (a)
del a[-1]
print(a)
a[2:5] = ['heloo']
print(a)
a[1:1] = ['a', 'b', 'c', 'd', 2.5]
print(a)
a += ['kiwi', 'graphs'] # This will append the list at the end of the list
print(a)
a = [10, 20] + a; print(a) # This will append list from the begining
#a += 30 # this can't be done, we cant add integer 
a += [30]; print(a)

b = ['spam', 'egg', 'bacon'] ; print(b)
b += 'tomato';print(b)
b[3:] = []; print(b) # deleting index value 3 to end
b += ['tomato']; print(b)