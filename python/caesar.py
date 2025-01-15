# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shift = 65 if char.isupper() else 97  # Determine the shift value based on uppercase or lowercase
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char  # Keep non-alphabetic characters as they are
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is alphabetic
            shift = 65 if char.isupper() else 97  # Determine the shift value based on uppercase or lowercase
            decrypted_text += chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted_text += char  # Keep non-alphabetic characters as they are
    return decrypted_text

# Main program
def main():
    while True:
        print("\n--- Caesar Cipher Program ---")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            key = int(input("Enter the encryption key (1-10): "))
            if 1 <= key <= 10:
                encrypted_text = caesar_encrypt(text, key)
                print(f"Encrypted Text: {encrypted_text}")
            else:
                print("Invalid key. Please enter a key between 1 and 10.")
        elif choice == "2":
            encrypted_text = input("Enter the text to decrypt: ")
            key = int(input("Enter the decryption key (1-10): "))
            if 1 <= key <= 10:
                decrypted_text = caesar_decrypt(encrypted_text, key)
                print(f"Decrypted Text: {decrypted_text}")
            else:
                print("Invalid key. Please enter a key between 1 and 10.")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Run the program
if __name__ == "__main__":
    main()