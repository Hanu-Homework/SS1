def translate_to_number(number_string: str):

    # The return value
    ret = ""

    # A constant ascii value of the character a
    a_ascii_index = ord("a")

    # Convert the input string to a lowercase version
    number_string = number_string.lower()

    # Iterate through all the characters in the string
    for char in number_string:

        # If the character is a number of a dash
        if '0' <= char <= '9' or char == '-':
            # Just add it to the return value
            ret += char

        else:
            # The relationship between an alphabetic character and its phone number value:
            # - When the alphabetic increases by 3 (for example, from A -> D), its phone number
            # will increase by 1.
            # - The phone value starts at 2, not zero, so we must add 2 to the converted version
            converted = (ord(char) - a_ascii_index) // 3 + 2

            # Add the converted version to the return value
            ret += str(converted)
    
    return ret


if __name__ == "__main__":
    print(translate_to_number("555-GET-FOOD"))
