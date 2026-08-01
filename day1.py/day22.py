try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Invalid input. Please enter a valid number.")
try:
    a = 10
    b = int(input("Enter a number: ")) 
    print(a/b)
except:
    print("Error: Division by zero is not allowed.")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result of division:", result)
except:
    print("Error: Division by zero is not allowed.")
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
    print("You entered:", num)
except ValueError as ve:
    print("Error:", ve)
try:
    num = int(input("Enter a number: "))
except:
    print("Invalid input. Please enter a valid number.")
else:
    print("You entered:", num)
try:
    num = int(input("Enter a number: "))
    print("Square = " ,num*num)
except:
    print("Invalid input.")
try:
    print("Hello")
except:
    print("Error")