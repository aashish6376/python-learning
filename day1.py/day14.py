attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    username = username.strip().upper()
    if len(username) < 3:
        print("Invalid username.")
    else: 
        password = input("Enter password: ")
        password = password.strip()
        if len(password) >= 8:
            print("Welcome", username)
            print("Strong password")
        else:
            print("Welcome", username)
            print("Weak password")
            attempts -= 1
            break
username = input("Enter username: ").strip().upper()
if len(username) < 3:
    print("username invalid.")
else:
    password = input("Enter password: ").strip()

    has_digit = False
    for i in password:
        if i.isdigit():
            has_digit = True
            break
    if len(password) < 8:
        print("Paasword should contain atleast 8 digits.")
    elif not has_digit:
        print("Password must contain atleast one digit.")
    else:
        print("Welcome", username)
        print("Strong password.")