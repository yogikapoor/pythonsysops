num = eval(input("Enter any number between 1-10 range: "))

num_word = {1: "one", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}

if num in num_word:
    print(f"{num_word.get(num)}")
else:
    print(f"The number {num} you have enter is out of range")