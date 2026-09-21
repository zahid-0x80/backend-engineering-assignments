user_name = "zahid@mail.com"
user_password = "1234"
user_name_input = input("Enter your username: ")
user_password_input = input("Enter your password: ")
if user_name_input == user_name:
    if user_password_input == user_password:
        print(f"Logged in as {user_name_input}")
    else:
        print(f"Login failed")
else:
    print(f"Login failed")