def pig_latin(string: str) -> str:
    # Convert the string to uppercase and split it into words
    words = string.upper().split(" ")

    # The return value
    ret = ""

    # Iterate through each words of the string
    for word in words:
        # Bring the first character to the end of the word
        # Add 'AY' to the end of the word
        pig_word = word[1:] + word[0] + 'AY'

        # Add an additional blank after each word to separate this word with the next word
        ret += pig_word + " "

    return ret


if __name__ == '__main__':
    # Get the string input from the user
    s = input("Enter a string: ")

    # Print out the result
    result = pig_latin(s)
    print(f"Result: {result}")
