import art  # Import the art module for logo display

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(start_text, key, cipher_direction):
    """
        Performs the Caesar cipher encryption or decryption.

        :param start_text: The input message to be encrypted or decrypted.
        :param key: The shift number to be applied.
        :param cipher_direction: The direction of encryption ('encode') or decryption ('decode').
    """
    new_letter = ''
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if key > 26:
            key %= 26
        if letter not in alphabet:
            end_text += letter
        elif cipher_direction == 'encode':
            new_letter = alphabet[position + key]
        elif cipher_direction == 'decode':
            new_letter = alphabet[position - key]
        end_text += new_letter
    print(f"The {cipher_direction}d text is {end_text}")


end = False  # Variable to control program flow
print(art.logo)  # Display the logo using art library

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode' or direction == 'decode':
        cipher(text, shift, direction)  # Call the cipher function with the provided inputs
    else:
        print("You entered wrong direction")  # Display an error message if an invalid direction is entered
    choose = input("Type 'yes' if you want to continue. Otherwise type 'no': ").lower()
    if choose == 'no':
        print("Goodbye")
        end = True  # Set the end variable to True to exit the program loop
