#!/usr/bin/python3
import subprocess
#import sys

cmd = "java -version"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()

if rc==0:
    print('Java Version:', err.splitlines()[0].split()[2].strip("\""))

# print(f" Java Version: {err.split()[2]}")




