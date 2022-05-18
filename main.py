from art import logo
import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction) -> str:
    end_text = ""

    if type(start_text) is not str:
        raise TypeError("Message accepts only string!")

    if not all(number in list(string.digits) for number in list(str(shift_amount))):
        raise TypeError("Shift amount accepts only integers!")

    if cipher_direction not in ["encode", "decode"]:
        raise ValueError("Cipher direction must be 'encode' or 'decode' only!")

    shift_amount = int(shift_amount) % 26

    if cipher_direction.lower() == "decode":
        shift_amount *= -1
    for char in start_text.lower():
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction} result: {end_text}")
    return end_text


print(logo)

end_of_test = True
while end_of_test:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = input("Type the shift number:\n")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        end_of_test = False
        print("Goodbye")
    else:
        end_of_test
