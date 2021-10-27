#!/usr/bin/python3
import os,sys,subprocess,platform

# if platform.system() is 'Linux':
#     cmd = 'cat newdemo.txt' # Linux
# else:
#     cmd = 'type newdemo.txt' # Window



# file_open = open("newdemo.txt","w")
# print(file_open.mode)
# print(file_open.readable())
# print(file_open.writable())
# file_open.close()
# print(os.listdir())

# file_open = open("newdemo.txt", 'w')
# file_open.write("This is a first line\n")
# file_open.write("Now second line\n")
# file_open.close()

my_content=['This is data -1\n', 'This is data -2\n', 'This is data -3']
file_open = open("newdemo.txt", 'w')
file_open.writelines(my_content)
file_open.close()

#cmd = 'cat newdemo.txt' # Linux 
#cmd = 'type newdemo.txt' # Window
if platform.system() == 'Linux':
    cmd = 'cat newdemo.txt' # Linux
else:
    cmd = 'type newdemo.txt' # Window
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()
print(platform.system())
print(out,err)