def count_vowels_and_consonants(string: str) -> tuple:
    all_vowels = ('a', 'e', 'i', 'o', 'u')

    vowels_count = 0
    consonants_count = 0

    for char in string.lower():
        if char in all_vowels:
            vowels_count += 1
        elif 'a' <= char <= 'z':
            consonants_count += 1

    return vowels_count, consonants_count


if __name__ == "__main__":
    s = input("Enter a string: ")
    vowels, consonants = count_vowels_and_consonants(s)

    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")
