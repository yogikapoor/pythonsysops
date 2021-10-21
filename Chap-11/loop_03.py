my_list = [1,2,3,4,6,7, "Hello World", 10.0]

for each in my_list:
    if type(each) == float:
        #print("Found your value : ", each)
        print(f"Found your value: {each}")
for each_range in range(1,10):
    if each_range %2:
        print(f"{each_range} its a odd Number ")
    else:
        print(f"{each_range} is a even number")
