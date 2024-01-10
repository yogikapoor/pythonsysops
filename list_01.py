'''
a = ['spam', 'egg', 'bacon', 'tomato']
b = ['egg', 'bacon', 'tomato', 'spam']
print ( a == b)
print ( a is b )

a1 = [2, 4, 6, 8]
print (type(a1))

ab = [21.42, 'spam', 3, 4, 'egg', False, 3.14159]
print(ab, type(ab))
print(a in b)

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = [2]
print (x == y)
print (z in y)
'''
a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

print (a[0])
print (a)
print( a[len(a)-1]) # Note length here is 6, so we need to -1. cos starting value is zero .

print(a [1:2:3])
print (a[0:6:2]) 
print(a[::-1]) # reverse the list
print('egg' in a)
print('spam' in a )
print('kiwi' not in a )
print('kiwi' in a )



























