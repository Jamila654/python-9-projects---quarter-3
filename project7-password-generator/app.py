import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

def get_user_input():
  try:
    length = int(input("Enter the desired password length (minimum 8): "))
    if length < 8:
        print("Password length must be at least 8. Setting to 8.")
        length = 8
    
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_letters, use_digits, use_special
  except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
    return get_user_input()

def generate_password(length, use_letters, use_digits, use_special):
    char_pool = ""
    password = []
    
    if use_letters:
        char_pool += letters
        password.append(random.choice(letters))
    if use_digits:
        char_pool += digits
        password.append(random.choice(digits))
    if use_special:
        char_pool += special_chars
        password.append(random.choice(special_chars))
    
    if not char_pool:
        char_pool = letters
        password.append(random.choice(letters))
        print("No character types selected. Using letters only.")
    
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))
    
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Random Password Generator!")
    length, use_letters, use_digits, use_special = get_user_input()
    password = generate_password(length, use_letters, use_digits, use_special)
    print(f"\nYour generated password is: {password}")


main()