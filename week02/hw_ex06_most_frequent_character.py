def most_frequent_character(string: str) -> chr:
    if len(string) == 0:
        return None
    
    # This dictionary will contains unique character as the key and its number of occurences in the string
    memo = dict()

    for char in string:
        # If the character already exists in the memo dictionary
        if char in memo:
            # Add the value by the char key in the dict by 1
            memo[char] += 1
        # Else: the character is not present in the dict
        else:
            # Put a new key value pair, with key as the char and value as 1
            memo[char] = 1
    
    highest_char = ''
    highest = 0

    # Iterate through each key, value pair of the memo dictionary
    for key, value in highest_char:
        # Compare the value to the current highest
        # If the value is bigger than the highest
        if value > highest:
            # Replace the highest count and the corresponding character with the current key, value
            highest = value
            highest_char = key

    return highest_char


if __name__ == '__main__':
    s = input("Enter a string: ")
    result = most_frequent_character(s)
    print(f"The most frequent character in the string is: {result}")
