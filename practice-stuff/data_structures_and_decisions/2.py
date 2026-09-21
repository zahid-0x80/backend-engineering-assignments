input_list = [10, 20, 30, 40, 50, 60, 70, 80]

user_input = int(input("Enter a number: "))

if user_input in input_list:
    print(f"{user_input} is in the list")
else:
    print(f"{user_input} is not in the list")