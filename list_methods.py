a = ['a', 'b']; print(a)
a.append(123); print(a)
x = a.append(45); print(x); print(type(x)) # x value will none coz list wont print out the result, it will update its list only
a.append([1,2,3]); print(a) # this result in nested list 
a.append('hello'); print(a) # this result will extend the list with string
a.extend([4,5,6]);print(a) # This result will extend the list ( Not a nested list)

b = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']; print(b)
#b.insert(3,3.122);print(b) # This will insert 3.122 value at 3rd index ( remember index starts with 0,1,2,3...
#b.remove('egg');print(b)
#b.clear(); print(b) # For empty the list
b.sort(); print(b) # Note: Sorting will start with CAPITAL "A - Z" then "small letters (a-z)"
c = ['bacon', 'egg', 'ham', 'lobster', 'spam', 'tomato', 'Apple', 'Zebra']
print(c); c.sort(); print(c)
c.sort(key=str.lower); print(c)
c.sort(key=str.upper); print(c)
c.sort(key=str.upper, reverse=True); print(c)




