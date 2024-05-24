import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine character sets based on complexity level
    all_chars = lower_case + upper_case + digits + symbols

    # Generate password using random.choices for Python 3.6+
    password = ''.join(random.choices(all_chars, k=length))
    
    return password

def main():
    # user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
