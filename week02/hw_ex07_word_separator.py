def word_separator(string: str) -> str:
    ret = ""

    for char in string:
        if 'A' <= char <= 'Z':
            ret += " " + char
        elif 'a' <= char <= 'z':
            ret += char

    return ret.lstrip()


if __name__ == '__main__':
    s = input("Enter a string: ")
    print(word_separator(s))
