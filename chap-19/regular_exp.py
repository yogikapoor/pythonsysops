import re
text = "This is a python lanugage @ and it is easy to learn"
my_pat=  "\w\w" # "[@asi]" # [abcd] or [a-d] # "i." # "i[st]""  #\w  means any char or number 

print(re.findall(my_pat,text))
print(len(re.findall(my_pat,text)))