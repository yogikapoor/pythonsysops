import os
t_w = os.get_terminal_size().columns
given_str = input("Enter your string: ")

print(given_str)
user_confirmation = input("Do you want to align your string ( Yes/No):  ")
if user_confirmation.title() == "Yes":
    print(given_str.center(t_w).title())
    print(given_str.ljust(t_w).title())
    print(given_str.rjust(t_w).title())

