#!/usr/bin/python3
import os,sys,subprocess

# file_open = open("newdemo.txt","w")
# print(file_open.mode)
# print(file_open.readable())
# print(file_open.writable())
# file_open.close()
# print(os.listdir())

file_open = open("newdemo.txt", 'w')
file_open.write("This is a first line\n")
file_open.write("Now second line\n")
file_open.close()
cmd = 'cat newdemoe.txt'
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()
print(out,err)