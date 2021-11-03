#!/usr/bin/python

sfile = "with_loop.txt"
dfile = "new_coppied.txt"

sfo = open(sfile)
print(sfo.mode)
content=sfo.read()
sfo.close()

dfo = open(dfile,'w')
dfo.write(content)
dfo.close
