import os
import sys
read_usr = input( " Enter your path :  ")
if os.path.exists(read_usr):
    usr_path = os.listdir(read_usr)
else:
    print(f"Please provide valid path")
    sys.exit()

print(f"{usr_path}")
print(f"{os.path.join(read_usr,usr_path[0])}")
print(f"{os.path.join(read_usr,usr_path[1])}")

for each_file in usr_path: 
    file_full_path = os.path.join(read_usr,each_file)
    if os.path.isfile(file_full_path):
        print(f"{each_file} is a file")
    else:
        print(f"{each_file} is a directory")
