import os, sys
from posixpath import join
age = 3
req_path = input("Enter the path : ")
if  not os.path.exists(req_path):
    print("Please provide valid path !!!")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path....!!")
    sys.exit(2)
for each_files in os.listdir(req_path):
    each_files_path = os.path.join(req_path,each_files)
    
