def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # Ensure shift stays within the range of the alphabet

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                new_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            result += new_char
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result


# Main program
print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose an option (1 or 2): ")

if choice not in ['1', '2']:
    print("Invalid choice! Exiting program.")
else:
    mode = "encrypt" if choice == '1' else "decrypt"
    message = input("Enter your message: ")
    shift_value = int(input("Enter the shift value: "))

    output = caesar_cipher(message, shift_value, mode)
    print(f"\nResult ({mode}ed text): {output}")
