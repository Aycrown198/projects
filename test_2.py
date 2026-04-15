import secrets
import string
import pyperclip

def generate_password(length=9):
    if length < 8:
        raise ValueError("Password must be at least 8 characters long")
    
    # Base character sets
    chars = string.ascii_lowercase + string.ascii_uppercase
    
    # Ensure at least one of each required type
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
    ]
    
    chars += string.digits
    password.append(secrets.choice(string.digits))
    chars += string.punctuation
    password.append(secrets.choice(string.punctuation))

    # Fill remaining length
    remaining_length = length - len(password)
    password.extend(secrets.choice(chars) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        number = int(input("Enter the desired numbers password: "))
        for _ in range(number):
            password = generate_password(length)
            print(password)
            # Automatically copy the last generated password to clipboard
            pyperclip.copy(password) 
            
        print("\nNote: The last password generated has been copied to your clipboard!")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid whole number.")
