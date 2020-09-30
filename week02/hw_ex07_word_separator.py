def word_separator(string: str) -> str:

    # The return value
    ret = ""

    # Iterate through each characters of the string
    for char in string:

        # If the character is a uppercase
        if 'A' <= char <= 'Z':
            # Add an additional blank before it
            ret += " " + char

        # Else if the character is a lowercase one
        elif 'a' <= char <= 'z':
            # Just add it to the return value ithout anything new
            ret += char

    return ret.lstrip()


if __name__ == '__main__':
    # Get the input string from the user
    s = input("Enter a string: ")

    # Print out the result
    print(word_separator(s))
