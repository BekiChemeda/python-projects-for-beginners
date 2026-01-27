import random
from string import punctuation, ascii_letters, digits

class EncryptionTool:
    def __init__(self):
        # Define the allowed characters including space, digits, punctuation, and letters
        self.chars = " " + digits + punctuation + ascii_letters
        self.chars = list(self.chars)
        self.keys = self.chars.copy()
        
        # Shuffle the keys to create the substitution mapping
        random.shuffle(self.keys)

    def encrypt(self, message):
        """Encrypt the message using the shuffled keys."""
        cipher = ""
        for letter in message:
            try:
                index = self.chars.index(letter)
                cipher += self.keys[index]
            except ValueError:
                # If character not in list, keep it as is
                cipher += letter
        return cipher

    def decrypt(self, cipher_text):
        """Decrypt the message using the shuffled keys."""
        plain_text = ""
        for letter in cipher_text:
            try:
                index = self.keys.index(letter)
                plain_text += self.chars[index]
            except ValueError:
                plain_text += letter
        return plain_text

def main():
    tool = EncryptionTool()
    
    print("Encryption Program Started.")
    
    while True:
        print("\n--- Menu ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Show Keys (Debug)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            encrypted = tool.encrypt(text)
            print(f"Encrypted text: {encrypted}")
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            decrypted = tool.decrypt(text)
            print(f"Decrypted text: {decrypted}")
        elif choice == '3':
            # Option to see the mapping, useful for understanding
            print(f"Warning: This reveals the encryption key!")
            print(f"Original: {''.join(tool.chars)}")
            print(f"Key:      {''.join(tool.keys)}")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()