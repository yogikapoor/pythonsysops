import subprocess

#cmd = 'ls -ltr'.split()
cmd = ['ls', '-ltr']
sp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()

print(f'The return code is : {rc}')
print(f'The output : \n{out.splitlines()}')
if err != 0:
    print(f'Error: \n{err.splitlines()}')


