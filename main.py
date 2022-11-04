international_morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', " ": "/"
}

print("Hint: Separate morse code by'/' and words by spaces.")


def convert_message(message_to_convert):
    if message_to_convert[0] in [".", "-"]:
        swap_code = {v: k for k, v in international_morse_code.items()}
        return "".join(swap_code[symbol] for symbol in message_to_convert.split(" "))
    return " ".join(international_morse_code[letter.capitalize()] for letter in message_to_convert)


def convert_again():
    while True:
        message = input("Type your message to convert: ")
        try:
            print(convert_message(message))
            answer = input("Do you want to convert again? Type yes or no: ").lower()
            if answer == "yes":
                convert_again()
            else:
                break
        except KeyError:
            print("Looks like there was an invalid input.")
            continue
        else:
            break


convert_again()
