# Get the input number from the user
num = int(input("Enter a number: "))


def calculate_digits_sum(number: int) -> int:
    """
    Return the sum of all digits in a number

    Args:
        number (int): the input number
    Returns:
        (int): the sum of all digits of the input number
    """

    # Return value
    ret = 0

    while number != 0:
        # Extract the last digit number and add it to ret
        ret += number % 10

        # Delete the last digit of the number
        number //= 10

    return ret


# Print out the sum result
print(
    f"The sum of all digits of the number {num} is: {calculate_digits_sum(num)}")
