import string

def encrypt(message: str, shift: int) -> str:
    encrypted_chars = []
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_chars.append(encrypted_char)
        else:
            encrypted_chars.append(char)
    encrypted_message = ''.join(encrypted_chars)
    return encrypted_message

def decrypt(message: str, shift: int) -> str:
    return encrypt(message, -shift)

def validate_shift(shift: int) -> None:
    if not isinstance(shift, int):
        raise ValueError("Shift value must be an integer.")
    if shift < 0 or shift > 25:
        raise ValueError("Shift value must be between 0 and 25.")

def sanitize_message(message: str) -> str:
    allowed_chars = string.printable[:-5]  # Exclude control characters and whitespaces
    sanitized_message = ''.join(char for char in message if char in allowed_chars)
    return sanitized_message

def CaeserCipher():
    print("\n---Caeser Cipher Encryption / Decryption---")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ")

    if choice == "1": action = "encrypt"
    elif choice == "2": action = "decrypt"
    else:
        print("Invalid choice.")
        return

    message = input("Enter a message: ")
    shift = int(input("Enter a shift value (0-25): "))

    try:
        validate_shift(shift)
        sanitized_message = sanitize_message(message)
        if action == "encrypt":
            result = encrypt(sanitized_message, shift)
        else:
            result = decrypt(sanitized_message, shift)
        print("Result:", result)
    except ValueError as e:
        print("Error:", str(e))
    
CaeserCipher()
