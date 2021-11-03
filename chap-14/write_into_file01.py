

my_content=['This is using loop -1', 'loop-2', 'loop-3']

fo = open("with_loop.txt", "w")

for each_line in my_content:
    fo.write(each_line +'\n')
    
fo.close()

