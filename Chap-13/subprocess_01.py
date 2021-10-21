import subprocess
cmd = 'ls -ltr'
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rc = sp.wait()
out,err=sp.communicate()

print(f"The return code: {rc}")
print(f"The Output : {out}")
print(f"The Error : {err}")