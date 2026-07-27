name = "aashish"
print(name.upper())
name = "AASHISH"
print(name.lower())
a = "BANANA"
print(a.replace("N" , "#"))
W = "I LOVE BANANA"
print(W.replace("BANANA" , "MANGO"))
a = "mango"
print(a.find("n"))
a = "dkgkjdfhfhd"
print(a.count("d"))
name = "   Aashish   "
print(name.strip())
name = input("Enter your name: ")
name = name.upper()
name = name.strip()
print("Hello", name)
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    username = username.strip().upper()
    if password == "1234":
        if len(username) <3:
            print("Invalid username.")
        elif username == "ADMIN":
            print("Access granted.")
            break
        else:
            print("Username not found.")
    else:
        print("Wrong password.")
    attempts -= 1
    print("Attempts left: ", attempts)
if attempts == 0:
    print("Account locked.")
attempts = 3
while attempts > 0:
    username = input("Enter username: ").strip().upper()
    if username.lower() == "exit":
        print("Programe closed.")
        break
    password = int(input("Enter password: "))
    if len(username) < 3:
        print("Invalid username.")
    elif username == "ADMIN":
        if password == 1234:
            print("Welcome Admin 😊!")
            break
        else:
            print("Wrong password.")
            attempts -= 1
            print("Attempts left: ", attempts)
    else:
        print("Username not found.")
        attempts -= 1
        print("Attempts left: ", attempts)
if attempts == 0:
    print("\n⚡ Account locked.")
    print("Please try again later.")