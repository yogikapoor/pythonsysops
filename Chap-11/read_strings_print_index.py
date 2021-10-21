import sys
usr_input = str(input("Enter the string value: "))
index_01 = 0
if usr_input is not False:
    print(usr_input)
    for each in usr_input:
        print(f"{each}--> {index_01}")
        index_01 = index_01 + 1
else:
    print(f"Please enter a string")
    sys.exit()

