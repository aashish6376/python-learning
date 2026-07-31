import random
number = random.randint(1,10)
print(number)
import random
secret = random.randint(1,10)
guess = int(input("Guess the number(1,10): "))
if guess == secret:
    print("Correct")
else:
    print("Wrong")
import random
secret = random.randint(1,10)
while True:
    guess = int(input("Guess the number(1,10): "))
    if guess == secret:
        print("Correct.")
        break
    elif guess < secret:
        print("Too low!")
        print("Try again🙃.")
    else:
        print("Too high!")
        print("Try again🙃.")
import random
secret = random.randint(1,20)
while True:
    guess = int(input("Guess the number(1,20): "))
    if guess == secret:
        print("Correct😊!")
        break
    elif guess< secret:
        print("Too low!")
        print("Try again🙃!")
    else:
        print("Too high!")
        print("Try again🙃!")