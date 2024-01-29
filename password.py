import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # User input: prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Generate password
    password = generate_password(length)

    # Display the password
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
