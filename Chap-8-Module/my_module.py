import platform as pt
print(f"System Kernel Details and OS release: {pt.platform()}")
print(f"Its is 32/64 Bit {pt.processor()}")
print(f"Python Version installed: {pt.python_version()}")
print(f"Kernel Version {pt.release()}")
print(f"Which OS {pt.system()}")
print(f"Machine Namde : {pt.node()}")

print(f"{dir(pt)}")
print(f"{pt.java_ver()}")