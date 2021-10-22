#!/usr/bin/python3
import subprocess
#cmd = ['bash', '--version']
cmd = 'bash --version'.split()
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
return_code = sp.wait()
out, err = sp.communicate()

if return_code ==0:
    print(f"Bash Version : {out.splitlines()[0].split()[3].split('(')[0]}")
    #print(type(out))
else:
    print(f'Error is : {err}')
