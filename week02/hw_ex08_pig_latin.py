def pig_latin(string: str) -> str:
    words = string.upper().split(" ")

    ret = ""
    for word in words:
        pig_word = word[1:] + word[0] + 'AY'
        ret += pig_word + " "

    return ret


if __name__ == '__main__':
    s = input("Enter a string: ")
    result = pig_latin(s)
    print(f"Result: {result}")
