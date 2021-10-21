import os,sys
list_dir_file = input(f"Enter files or directory you want to delete: ")
# into_list = [list_dir_file]
# print(list_dir_file, into_list)
for each_file in list_dir_file:
    if os.path.isfile(each_file):
        os.remove(each_file)
    else:
        print(f"Its a directory : {each_file}")
