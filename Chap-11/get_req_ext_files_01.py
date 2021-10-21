import os,sys
req_path=input(f"Enter your directory path: ")
if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file. Please entry only directory path")
    sys.exit()
else:
    all_file_dir= os.listdir(req_path)
    if len(all_file_dir) == 0:
        print(f"The given path is empty {req_path}")
        sys.exit()
    else:
        req_ext=input(f" Enter the required files extenion .py .sh .log .txt: ")
        file_list = []
        for each_file in all_file_dir:
            if each_file.endswith(req_ext):
                file_list.append(each_file)
        if len(file_list) == 0:
            print(f"No files found with {req_ext} extension")
            sys.exit()
        else:
            print(f"Found {len(file_list)} files with the {req_ext} extension ")
            print(f"Your files are : ",file_list)
