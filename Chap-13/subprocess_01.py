import subprocess
# if you want to pass your cmd as a string then you need to SHELL = True (eg:- 'ls -ltr' )else shell shell = False / When mention Shell equal to True, python will open new shell while executing the cmd. 
# If shell equal to False, its will be list (eg:- ['ls', '-lrt']). 
cmd = 'dir'
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rc = sp.wait()
out,err=sp.communicate()

print(f"The return code: {rc}")
print(f"The Output : {out}")
print(f"The Error : {err}")

