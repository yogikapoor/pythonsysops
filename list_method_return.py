a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']; print(a)
a.pop();print(a) # by default pop will pop the value from -1 index ( last value from the list)

b = a.pop(); print(f" print a list : {a}, \nNow printing b value:  {b}") # Advantage with list pop is it returns a value and you print or store it in new variable 
print(a.pop(-2))

# with index option you can search the object value in the list
print(a); print(a.index('spam')) # searching for spam index value
print(a[a.index('spam')]) # Searching for "spam" index value and printing it

# count option this will allow you to count no of times values found in a list
b = [2, 4, 6, 8, 6, 4, 6, 2, 100]; print(b.count(2)); print(b.count(6))