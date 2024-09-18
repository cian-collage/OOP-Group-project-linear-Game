"""
Program Name: decipher_decryption_game.py

Program Description:

This is a minigame module in the game that the players play to engage themselves in the user experience
The user receives an encrypted message with Caesar's Cipher.
The user is prompted to guess a shift value to unravel a secret message.
The user will have a limited number of attempts to decrypt the message

Author: Max Ceban
Date: 27/11/2023
"""

import random


# This method encrypts a message for the user to try and decrypt
def encrypt_message(message, shift):
    # Initialise an empty string
    encrypted_message = ""

    # Iterate through each character in the input message
    for char in message:
        # Check if the character is an alphabetical character
        if char.isalpha():
            # Determines the case of the character a shifts it accordingly
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 +
                               ord('a' if char.islower() else 'A'))
            # Appends the shifted character to the encrypted message
            encrypted_message += shifted_char
        else:
            # If the character is not an alphabetical character, leave it unchanged
            encrypted_message += char
    # Returns the encrypted message
    return encrypted_message


def get_user_guess():
    while True:
        guess = input("Enter your guess (shift value): ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Invalid Input. Please enter a number.")


def decrypt_message(encrypted_message, shift):
    decrypted_message = encrypt_message(encrypted_message, -shift)
    return decrypted_message


def cipher_decryption_game():
    print("Welcome to the Cipher Decryption Game!")

    # This is the original message for the user to decrypt
    original_message = "The Legendary Witch Slayer will save us all"

    # Generates the shift bit to scramble the original message
    shift = random.randint(1, 25)
    # print(shift)

    # Attempts user has taken
    attempts = 0

    hint = ""

    # encrypts the message
    encrypted_message = encrypt_message(original_message, shift)

    print(f"Encrypted Message: {encrypted_message}")

    while True:
        # User attempts to decrypt the message
        user_guess = get_user_guess()

        # Checks if the user's guess is correct
        decrypted_message = decrypt_message(encrypted_message, user_guess)

        if decrypted_message == original_message:
            print(f"Congratulations! You successfully decrypted the message {original_message}")
            break
        else:
            print(f"Sorry, your guess is incorrect.\n")
            if attempts != len(original_message):
                hint = hint + original_message[attempts]
                print(f"Hint: {hint}")
                print("Time's arrow may point ahead, but wisdom often hides in the echoes of its reverse dance.")
                print(f"Encrypted Message: {encrypted_message}")
                attempts += 1
            else:
                print(f"Sorry, your guess is incorrect.\n")
                print(f"Hint: {hint}")
                print("Time's arrow may point ahead, but wisdom often hides in the echoes of its reverse dance.")
                print(f"Encrypted Message: {encrypted_message}")


if __name__ == "__main__":
    cipher_decryption_game()
