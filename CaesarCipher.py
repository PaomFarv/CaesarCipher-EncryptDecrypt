#Caesar Cipher Text Encryption & Decryption (Julius Caesar)
def caesar_cipher_encrypt(text, shift):
    result = ""
    shift_value = shift % 26  # Ensure shift is within alphabet range

    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            if char.islower():  # Encrypt lowercase characters
                new_char = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
            elif char.isupper():  # Encrypt uppercase characters
                new_char = chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
            result += new_char
        else:
            result += char  # Preserve non-alphabetic characters as is

    return result

# Function to decrypt text by reversing the shift
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Main program loop for user interaction
print("Welcome to the Caesar Cipher text encrypter and decrypter program.")
print("Developed by PaomFarv.")
print("\nType (E) to Encrypt text.\nType (D) to Decrypt text.\nType (Q) or press Enter to quit.")

while True:
    user_response = input("\nYour response (E, D, Q): ").strip().upper()
    
    if user_response == "E":
        text = input("Enter the text to encrypt (case-sensitive): ")
        
        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))  # Ensure shift is an integer
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")

        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Encrypted Text:", encrypted_text)

    elif user_response == "D":
        text = input("Enter the text to decrypt (case-sensitive): ")

        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))  # Ensure shift is an integer
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")
        
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print("Decrypted Text:", decrypted_text)

    elif user_response == "Q" or user_response == "":
        print("You have exited the program.")  # Exit the program
        break
    
    else:
        print("Invalid Input. Please try again.")  # Handle invalid options