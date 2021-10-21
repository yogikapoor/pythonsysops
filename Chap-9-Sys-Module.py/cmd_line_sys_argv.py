#!/usr/bin/python3
import sys
if len(sys.argv) != 3:
    print(f"Usage:")
    print(f"{sys.argv[0]} <your_required_string> <lower/upper/title>")
    sys.exit()
usr_string=sys.argv[1]
usr_action=sys.argv[2]

#print(f"{usr_string}")

if usr_action.lower() == "lower":
    print(usr_string.lower())
elif usr_action.lower() == "upper":
    print(usr_string.upper())
elif usr_action.lower() == "title":
    print(usr_string.title())
else:
    print("Your option is invalid. Please select valid options from this list: lower/upper/title")
