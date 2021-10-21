import os
path = input("Enter your path: ")

if os.path.exists(path):
    print(f" Given path : {path} is a valid path")
    if os.path.isfile(path):
        print(f"The given path {path} is a file ")
    else:
        print(f"The given path {path} is a directory")
else:
    print(f"Given path : {path} doesn\'t exist")

