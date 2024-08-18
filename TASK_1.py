def encrypt(text, shift):
    """
    Encrypt the text using Caesar Cipher with the given shift.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift character within the bounds of ASCII values for letters
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def decrypt(text, shift):
    """
    Decrypt the text using Caesar Cipher with the given shift.
    """
    return encrypt(text, -shift)

def main():
    while True:
        operation = input("Would you like to encrypt or decrypt a message? (Enter 'e' for encryption, 'd' for decryption, or 'q' to quit): ").lower()
        if operation == 'q':
            break
        elif operation in ['e', 'd']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            
            if operation == 'e':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid operation. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
