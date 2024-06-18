def caesar_encrypt(plaintext, shiftkey):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shiftkey % 26
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(plaintext, shiftkey):
    return caesar_encrypt(plaintext, -shiftkey)

while True:
    choice = input("Do you want to (e)ncrypt, (d)ecrypt, or (x)it?: ").strip().lower()
    
    if choice == 'x':
        print("Exiting the program.")
        break

    plaintext = input("Enter the plaintext: ").strip()

    while True:
        try:
            shiftkey = int(input("Enter the shift key (0-25): ").strip())
            if 0 <= shiftkey <= 25:
                break
            else:
                print("Please enter a valid shift key between 0 and 25.")
        except ValueError:
            print("Please enter a valid integer for the shift key.")

    if choice == 'e':
        print("Encrypted text:", caesar_encrypt(plaintext, shiftkey))
    elif choice == 'd':
        print("Decrypted text:", caesar_decrypt(plaintext, shiftkey))
    else:
        print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'x' to exit.")
