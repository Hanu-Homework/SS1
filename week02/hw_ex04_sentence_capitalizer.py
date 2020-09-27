def capitalized(string: str) -> str:
    return string[0].upper() + string[1:]


def capitalize_all(para: str) -> str:

    # The return value
    ret = ""

    #
    sentences = para.split(". ")

    for sentence in sentences[:-1]:

        ret += capitalized(sentence) + ". "

    ret += capitalized(sentences[-1])

    return ret


if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    