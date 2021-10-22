#!/usr/bin/python3
import subprocess
cmd = ['bash', '--version']
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
return_code = sp.wait()
out, err = sp.communicate()

if return_code ==0:
    print(f'out is: {out}')
else:
    print(f'Error is : {err}')