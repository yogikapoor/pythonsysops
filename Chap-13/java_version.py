#!/usr/bin/python3
import subprocess
#import sys

cmd = "java --version"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = sp.communicate()

print(f" Java Version: {err.splitlines}")

