def count_vowels_and_consonants(string: str) -> tuple:
    # A constant tuple holding all of the vowels
    all_vowels = ('a', 'e', 'i', 'o', 'u')

    vowels_count = 0
    consonants_count = 0

    # Convert all the characters of the string to lowercase
    string = string.lower()

    # Iterate through each characters of the string
    for char in string:

        if char in all_vowels:
            vowels_count += 1
        # Else if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            consonants_count += 1

    return vowels_count, consonants_count


if __name__ == "__main__":
    s = input("Enter a string: ")
    vowels, consonants = count_vowels_and_consonants(s)

    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")
