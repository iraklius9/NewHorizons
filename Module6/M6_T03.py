def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text


user_text = input("Enter text to encrypt: ")
user_shift = int(input("Enter shift value: "))

if user_shift < 0 or user_shift > 25:
    print("Shift value must be between 0 and 25")
else:
    print(caesar_cipher(user_text, user_shift))
