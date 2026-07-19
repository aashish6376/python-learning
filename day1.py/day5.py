count = 1
while count <= 5:
    print(count)
    count = count + 1
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
for i in range(1, 10, 2):
    print(i)
num = int(input("Enter your number: "))
while num != 7:
    print("try again.")
    num = int(input("Enter your number again: "))
print("correct number!")
attempts = 0
while attempts < 3:
    guess = int(input("Guess the number: "))
    if guess == 7:
        print("You guessed it right!")
        break
    else:
        print("Try again.")
    attempts = attempts + 1  
    print("You have used", attempts, "attempts.")