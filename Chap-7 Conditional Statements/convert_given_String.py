usr_str = input("Enter your string :  ")
usr_cnf = input("Do you want to convert your string to lower case(Yes/No) : ")

if usr_cnf.lower() == "yes":
    print(f"Your string is : {usr_str.lower()}")
else:
    print(f"Your string as is: {usr_str}")
