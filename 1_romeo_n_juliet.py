
# Phase 1: Get Sense Hat to flash out Morse Code.

from time import sleep
from sense_hat import SenseHat # For When on Pi, otherwise comment out

sense = SenseHat()

TERMINAL_COLORS = {
    "BLUE": "\033[94m",  # Blue text color for terminal
    "PINK": "\033[95m",  # Pink/Magenta text color for terminal
    "RESET": "\033[0m"   # Resets the color back to default
}

SENSEHAT_COLORS = {
    "BLUE": (0, 0, 255),  # Blue color for SenseHat (RGB tuple)
    "PINK": (255, 105, 180) # Pink color for SenseHat (RGB tuple)
}

# Adjust TIME_UNIT as needed.
# .13 is a Morse Code standard for human operators to send and read
# Smaller unit = Faster / Larger unit = Slower
TIME_UNIT = .13

# Time in seconds for each Morse Code symbol or spacing.
MORSE_CODE_UNITS = {
    ".": 1*TIME_UNIT,
    "-": 3*TIME_UNIT,
    "space_dot_dash": 1*TIME_UNIT,
    "space_letters": 3*TIME_UNIT,
    "space_words": 7*TIME_UNIT
}

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

def flash_morse_unit(RGB_color, morse_code):
    for symbol in morse_code:
        if symbol == "/":
            sleep(MORSE_CODE_UNITS["space_words"])
            
        if symbol == ".": 
            sense.clear(RGB_color)
            sleep(MORSE_CODE_UNITS["."])
            sense.clear()
            sleep(MORSE_CODE_UNITS['space_dot_dash'])
            
        if symbol == "-": 
            sense.clear(RGB_color)
            sleep(MORSE_CODE_UNITS["-"])
            sense.clear()
            sleep(MORSE_CODE_UNITS['space_dot_dash'])
            
    sleep(MORSE_CODE_UNITS['space_letters'])
    

for lines in dialogue:
    actor = lines[0]
    print(actor) # Name
    # for char in lines[1]:
    #     sleep(.05)
    #     print(f"{morse_code_dict[char.upper()]} ", end = "", flush=True) # flush keeps output from buffering, i.e. one letter at a time will be printed
    # print("\n")
    if actor == "ROMEO":
        color = SENSEHAT_COLORS['BLUE']
    elif actor == "JULIET":
        color = SENSEHAT_COLORS['PINK']
    else: 
        color = SENSEHAT_COLORS['BLUE']
    for char in lines[1]:
        print(char, morse_code_dict[char.upper()])
        flash_morse_unit(color, morse_code_dict[char.upper()])
