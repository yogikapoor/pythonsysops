import os,sys
usr_path = input("Enter your path: ")
req_ext = input("Provide file Extension for a search: eg: .py .sh .log .txt")

# Validate the user input
if os.path.isfile(usr_path):
    print(f"Invalid, please provide complete path not a file")
    sys.exit()
else:
    list_file = os.listdir(usr_path)
    for file_name in os.path.join(usr_path,list_file):
        print(f"{file_name}")



