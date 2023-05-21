# Python Caeser Cypher Encryption Algorithm
## Screenshot
![image](https://github.com/petermartens98/Python-Caeser-Cypher-Encrypyion-Algorithm/assets/87671757/014ca8c6-5a2a-4431-86d3-fbc639e145df)

## Description
Python application that implements the Caesar cipher algorithm. It provides a user-friendly interface to encrypt messages by shifting each letter by a specified amount. The program takes a user input message and a shift value between 0 and 25 (inclusive), applies the encryption algorithm, and displays the encrypted message.

The Caesar cipher is a substitution cipher that replaces each letter in the message with another letter a fixed number of positions down the alphabet. For example, if the shift value is 3, 'A' becomes 'D', 'B' becomes 'E', and so on. Non-alphabetical characters in the message remain unchanged.

The program includes input validation to ensure that the shift value is within the valid range and handles exceptions gracefully. It also sanitizes the input message, removing unsupported characters to ensure compatibility with visible and printable characters.

The encryption program is easy to use, making it suitable for basic encryption needs where a simple and quick encryption method is required. It can be used for educational purposes or as a starting point for more advanced encryption algorithms.
## Requirements
- Python 3

## How It Works

1. The program prompts the user to enter a message and a shift value.
2. The `encrypt()` function applies the Caesar cipher algorithm by shifting each letter by the specified amount. The shift is performed separately for lowercase and uppercase letters, and non-alphabetical characters are left unchanged.
3. The `validate_shift()` function checks the validity of the shift value, ensuring that it is an integer between 0 and 25.
4. The `sanitize_message()` function removes unsupported characters from the message, keeping only visible and printable characters.
5. The main program calls the necessary functions to validate the input, sanitize the message, encrypt it, and display the encrypted message.
6. Error handling is implemented to catch and handle any exceptions related to invalid input or unsupported characters.

