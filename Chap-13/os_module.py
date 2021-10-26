#!/usr/bin/python3
import os

print(os.getcwd())
os.chdir(os.environ.get('HOME'))
print(os.getcwd())
print(os.listdir())
print(os.listdir("/home"))
os.mkdir("test")
os.removedirs("test")
print(os.listdir())
os.makedirs("abc/def")
os.rename("abc","abc123")
print(os.environ.get('HOME'))
#os.path.join()
os.path.exists('HOME')
