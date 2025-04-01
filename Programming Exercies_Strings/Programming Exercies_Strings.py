
#Task1. Remove punctuations
import string

# Ask the user to enter a paragraph
text = input("Type in a paragraph of text:\n")

# Create an empty string to store the result
no_punctuation = ""

# Check each character in the input
for char in text:
    # Only keep characters that are not punctuation
    if char not in string.punctuation:
        no_punctuation += char

# Output the cleaned text
print("\nText without punctuation:")
print(no_punctuation)



#Task2. Torrens University password requirements
# Ask user to input a password
password = input("Enter a string as a password: ")

# Define allowed special characters
special_chars = "!%@#"

# Initialize condition checks
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

# Check password length
if 8 <= len(password) <= 16 and has_upper and has_lower and has_digit and has_special:
    print("It satisfies Torrens University password requirements")
else:
    print("It does not satisfy Torrens University password requirements")
    
    
    
#Task3. Caesar Ciphe  
# Ask the user to enter the plaintext
plaintext = input("Enter the plain text:\n")

# Ask for the number of positions to shift (right)
shift = int(input("Enter the number of shifts:\n"))

# Initialize the ciphertext result
ciphertext = ""

# Loop through each character in the plaintext
for char in plaintext:
    if char.isalpha():  # Check if it's a letter
        # Shift within uppercase or lowercase separately
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        ciphertext += encrypted_char
    else:
        # If not a letter (e.g., space or punctuation), keep it unchanged
        ciphertext += char

# Output the final encrypted text
print("Encrypted text (ciphertext):")
print(ciphertext)

