# user will be asked what the password is until the user puts the correct password (unlimited attempts)
correct_password = "12345"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Wrong password. Try again.")

# 5 attempts only
correct_password = "12345"
attempts = 5

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. Attempts left: {attempts}")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")