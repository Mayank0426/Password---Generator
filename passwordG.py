"""
===========================================
 Secure Password Generator (Python Project)
===========================================

Features:
- Generate strong random passwords
- User-defined length and character types
- Multiple password generation
- Password strength checker
- Beginner-friendly and modular code

Author: Student Project
===========================================
"""

import string
import secrets


# -------------------------------
# Function to generate password
# -------------------------------
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("❌ You must select at least one character type!")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# -------------------------------
# Function to check strength
# -------------------------------
def check_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "💪 Strong"
    elif length >= 8 and score >= 2:
        return "⚡ Medium"
    else:
        return "⚠️ Weak"


# -------------------------------
# Main Program (CLI)
# -------------------------------
def main():
    print("\n🔐 Secure Password Generator 🔐\n")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        count = int(input("How many passwords to generate?: "))
        if count <= 0:
            raise ValueError

        print("\n🔑 Generated Passwords:\n")

        for i in range(count):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            strength = check_strength(pwd)
            print(f"{i+1}. {pwd}  --> {strength}")

    except ValueError:
        print("❌ Invalid input! Please enter valid values.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()