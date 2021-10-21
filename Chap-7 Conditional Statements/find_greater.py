usr_num01 = eval(input("Enter your frist number : "))
usr_num02 = eval(input("Enter your second number : "))

if usr_num01 > usr_num02:
    print(f" {usr_num01} is great then {usr_num02}")
elif usr_num01 < usr_num02:
    print(f" {usr_num01} is less then {usr_num02}")
else:
    print(f"{usr_num01} is equal to {usr_num02}")
