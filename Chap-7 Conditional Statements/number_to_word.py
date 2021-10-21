num = eval(input("Enter any number between 1-10 range: "))

if num in [1,2,3,4,5,6,7,8,9,10]:
    if num ==1:
        print("One")
    elif num == 2:
        print("Two")
    elif num == 3:
        print("Three")
    elif num == 4:
        print("Four")
    elif num == 5:
        print("Five")
    elif num == 6:
        print("Six")
    elif num == 7:
        print("Seven")
    elif num == 8:
        print("Eight")
    elif num == 9:
        print("Nine")
    else:
        print("Ten")
else:
    print(f"The Number {num} you have enter is out of range")

