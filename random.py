
MAX_ATTEMPTS = 3
PASSWORD = "secret123"

def main():
	attempts = 0
	while attempts < MAX_ATTEMPTS:
		ans = input("Enter password: ")
		if ans == PASSWORD:
			print("Access granted")
			return
		attempts += 1
		if attempts < MAX_ATTEMPTS:
			print("Wrong password, try again.")
	print("Account locked")

if __name__ == "__main__":
	main()
