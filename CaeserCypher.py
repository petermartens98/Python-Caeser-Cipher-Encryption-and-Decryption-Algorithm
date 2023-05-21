import string

def encrypt(message: str, shift: int) -> str:
    """
    Encrypts the message using the Caesar cipher with the specified shift value.
    
    Args:
        message (str): The message to be encrypted.
        shift (int): The shift value for the encryption.
    
    Returns:
        str: The encrypted message.
    """
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

def validate_shift(shift: int) -> None:
    """
    Validates the shift value.
    
    Args:
        shift (int): The shift value to be validated.
    
    Raises:
        ValueError: If the shift value is not an integer or not within the range of 0-25.
    """
    if not isinstance(shift, int):
        raise ValueError("Shift value must be an integer.")
    if shift < 0 or shift > 25:
        raise ValueError("Shift value must be between 0 and 25.")

def sanitize_message(message: str) -> str:
    """
    Sanitizes the message by removing unsupported characters.
    
    Args:
        message (str): The message to be sanitized.
    
    Returns:
        str: The sanitized message.
    """
    allowed_chars = string.printable[:-5]  # Exclude control characters and whitespaces
    sanitized_message = ''.join(char for char in message if char in allowed_chars)
    return sanitized_message

def main() -> None:
    """
    Main function to execute the encryption program.
    """
    print("---Python Caeser Cypher Encryption Algorithm---")
    message = input("Enter a message: ")
    shift = int(input("Enter a shift value (0-25): "))

    try:
        validate_shift(shift)
        sanitized_message = sanitize_message(message)
        encrypted_message = encrypt(sanitized_message, shift)
        print("Encrypted message:", encrypted_message)
    except ValueError as e:
        print("Error:", str(e))

if __name__ == '__main__':
    main()
