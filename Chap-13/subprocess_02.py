#!/usr/bin/python3
import subprocess

p1 = subprocess.run(['ls','-ltr'], shell=True, capture_output=True)
print(p1)
print(p1.args, p1.returncode)
print(p1.stdout) # to capture the out you need to use capture_output

# p2 = subprocess.run()
