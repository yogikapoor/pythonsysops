#!/usr/bin/python3
import subprocess

cmd = 'java -version'.split()
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
return_code = sp.wait()

out, err = sp.communicate()

if return_code == 0:
    print(f'Java Version: {err.splitlines()[0].split()[2]}')
else:
    print(f"Error : {out}")