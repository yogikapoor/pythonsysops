import subprocess

cmd = 'dir' #'ls -lrt' # shell should be True

# To aviod Error output as byte add Universal
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

return_code = sp.wait()
out,err = sp.communicate()

print( f' Your command is {cmd} ')
# in order to conver your output from string to list use ' splitlines()
print(f'Your command output is: {out.splitlines()}')
if err != 0:
    print(f'Your command error is : {err.splitlines()}')
