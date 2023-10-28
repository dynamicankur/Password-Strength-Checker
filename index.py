import re

def check_password_strength(password):
    # Minimum password length
    min_length = 8

    # Check if the password meets the minimum length requirement
    if len(password) < min_length:
        return "Weak: Password is too short."

    # Check for the presence of different character types
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\]', password)

    # Assess password strength based on character types
    if has_lowercase and has_uppercase and has_digit and has_special:
        return "Very Strong: Password meets all criteria."
    elif has_lowercase and has_uppercase and has_digit:
        return "Strong: Password is missing special characters."
    elif has_lowercase and has_uppercase:
        return "Moderate: Password is missing digits and special characters."
    else:
        return "Weak: Password is missing uppercase letters, digits, and special characters."

# Input: Get the password from the user
password = input("Enter a password: ")
result = check_password_strength(password)
print("Password Strength:", result)
