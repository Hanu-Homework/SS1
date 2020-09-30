def capitalized(string: str) -> str:
    """
    Convert the first character of the given string into uppercase.

    Args:
        string (str): the string to be capitalized

    Returns:
        str: the capitalized string
    """
    return string[0].upper() + string[1:]


def capitalize_all(para: str) -> str:
    # The return value
    ret = ""

    # Split the paragraph into sentences
    sentences = para.split(". ")

    # Iterate through each sentence to the last - 1 sentence
    # Because we are adding a dot after each capitalized sentences
    for sentence in sentences[:-1]:

        # Capitalize the sentence and add it with a dot to the return value
        ret += capitalized(sentence) + ". "

    # Add the last capitalized without the dot
    ret += capitalized(sentences[-1])

    return ret


if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
