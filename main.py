from microbit import *

import radio

def shift_letter(letter: str, amount: str) -> str:
    if (letter == ' '):
        return ' '
    letter_num = ord(letter.upper()) - ord('A')
    shifted_letter_num = (letter_num + amount) % 26
    return chr(ord('A') + shifted_letter_num)

def shift_message(message: str, amount: str) -> str:
    shifted_message = map(lambda l: shift_letter(l, shift_amount), message)
    return ''.join(shifted_message)

radio.on()
radio.config(channel=7) # Choose your own channel number

shift_amount = 5 # Choose the number of letters to shift by

while True:
    if button_a.was_pressed():
        radio.send(shift_message("Rodriguez", shift_amount)) # Change this to your name!

    new_message = radio.receive()
    if new_message:
        display.scroll(new_message)