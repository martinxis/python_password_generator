import random
import string

special_characters = "!@#$%^&*()_+=-[]{}|:;<>,.?/~"

def ask_pass_length():
    while True:
        try:
            pass_length = int(input("How long do you want your password to be (in numbers)?: "))
            if pass_length > 0:
                return pass_length
            else:
                print("Please enter a positive number for password length.")
        except ValueError:
            print("Please enter a valid number for password length.")

def generate_password(length):
    password = ""
    characters = string.ascii_letters + string.digits + special_characters
    for i in range(length):
        password += random.choice(characters)
    return password


def password_strength(password):
    if len(password) < 8:
        return "weak"
    elif any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
        if len(password) <= 12:
            return "medium"
        else:
            return "strong"
    else:
        return "weak"

if __name__ == "__main__":   
    password_length = ask_pass_length()
    generated_password = generate_password(password_length)
    password_final_strength = password_strength(generated_password)
    print(generated_password)
    print(f"Generated password's strength level is: {password_final_strength}")
