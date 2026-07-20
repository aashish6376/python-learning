while True:
    a = int(input("enter your number:"))
    if a > 0:
        print("Positive number.")
    elif a < 0:
        print("Negative number.")
    else:
        print("The end.")
        break
while True:
    a = int(input("Enter your number:"))
    if a > 100:
        print("Too large.")
    elif a < 100:
        print("Too small.")
    else:
        print("Correct.")
        break
attempts = 0
while attempts < 3:
    password = input("Enter password:")
    if password == "python123":
        print("Access granted")
        break
    else:
        print("try again.")
    attempts = attempts + 1
if attempts >= 3:
    print("Account locked.")