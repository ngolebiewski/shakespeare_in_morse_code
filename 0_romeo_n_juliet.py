
# next iteration, lets make a class for the dialogue. {actor: ROMEO, dialogue: blah blah blah, stage direction?}
dialogue = [("ROMEO", "Have not saints lips, and holy palmers too?"),
            ("JULIET", "Ay, pilgrim, lips that they must use in prayer.")]

morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..-..', '!': '-.-.--', '-': '-....-',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', '@': '.--.-.',
    '"': '.-..-.',  '\'': '.----.',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '_': '..--.-', '$': '...-..-', '%': '-----',  ' ': '/' # Space character
}

for lines in dialogue:
    print(lines[0]) # Name
    for char in lines[1]:
        print(f"{morse_code_dict[char.upper()]} ", end = "")
    print("\n")
