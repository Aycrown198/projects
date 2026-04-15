# Password Generator

A simple Python-based password generator that creates secure, random passwords with a mix of character types.

## Features

- Generates passwords with lowercase letters, uppercase letters, digits, and special characters
- Ensures at least one character from each required type for better security
- Uses Python's `secrets` module for cryptographically secure random number generation
- Shuffles the password to avoid predictable patterns
- Minimum password length of 8 characters
- Automatically copies the last generated password to the clipboard using `pyperclip`

## Requirements

- Python 3.x
- `pyperclip` library (install via `pip install pyperclip`)

## Usage

1. Run the script:
   ```
   python password_generator.py
   ```

2. Enter the desired password length (must be at least 8).

3. Enter the number of passwords to generate.

4. The passwords will be printed to the console, and the last one will be copied to your clipboard.

## Example

```
Enter the desired password length: 12
Enter the desired numbers password: 3
aB3!kL9@mN2p
X7$yT4&vQ1wZ
H5^nR8*oF6sD

Note: The last password generated has been copied to your clipboard!
```

## Files

- `password_generator.py`: The main secure password generator script.
- `password_generator_2.py`: A simpler version using `random` module (less secure).

## Security Notes

This tool uses `secrets` for randomness, which is suitable for cryptographic purposes. However, always follow best practices for password management and storage.