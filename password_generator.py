import random as random

def main():
    allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*(){"

    # Asking the user for the length of password 
    password_length = int(input("Enter the length of the password : "))

    # Creating the password of the desired length
    password = "".join(random.sample(allowed_characters,password_length))

    print(f"Your Password is {password}")

if __name__ == '__main__':
    main()
