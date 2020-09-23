# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def convert_to_morse_code(string: str) -> str:
    """
    Return the morse code version of a given string

    Args:
        string (str): the string to be converted
    Returns:
        (str): the morse code version of the given string
    """

    # Using the global dictionary that has been declared outside this function
    global MORSE_CODE_DICT

    # Return value
    ret = ""

    # Convert all of the characters to uppercase
    string = string.upper()

    # Iterate through all characters of the string
    for char in string:
        # If the morse code dictionary has the char key
        try:
            # Add the dictionary value corresponding to the key to the return value
            ret += MORSE_CODE_DICT[char]

        # Else if the char key does not exist in the dictionary
        except KeyError:
            # If this character is the space character
            if char == ' ':
                # Add the space to the return value
                ret += ' '

            # Else do nothing

    return ret


# Get the input string from the user
raw = input("Enter a string to convert: ")

# Display the morse code version of the given string
print(f"Morse code version: {convert_to_morse_code(raw)}")