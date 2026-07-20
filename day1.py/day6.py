pin = (input("Enter pin: "))
while pin != 4321:
    print("Try again.")
    pin = int(input("Enter again: "))
print("Access granted.")
attempts = 0
while attempts <3:
    pin = int(input("Enter pin:"))
    if pin == 4321:
        print("Access granted.")
        break
    else:
        print("Try again.")
    attempts= attempts = 1
f = 0 
while f<5:
    pin = int(input("enter your number:"))
    if pin == 7:
        print("Correct.")
        break
    else:
        print("Try again.")
    f = f+1
    print("You have used", f , "attempts.")