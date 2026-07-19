Username = input("Enter your username:")
Password = input("Enter your password:")
if Username == "admin" and Password == "1234" :
    print("Login successful")
else:print("Login failed")
day = "monday"
if day == "saturday" or day == "sunday": print("Today is a holiday")
else: print("Today is a working day")
logged_in = True
if not logged_in:
    print("Please log in to continue")
else:
    print("Welcome back!")
Username = input("Enter your username:")
Password = input("Enter your password:")
if Username == "admin":
    if Password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")
username = input("Enter your username:")
password = input("Enter your password:")
balance = int(input("Enter your account balance:"))
if username == "admin":
    if password == "1234":
        if balance >= 1000:
            print("Access granted.")
        else:
            print("Insufficient balance.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")