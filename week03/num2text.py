# A constant dictionary holding the translations for all the numbers from 0 to 9
num_text = {
    0: "Không",
    1: "Một",
    2: "Hai",
    3: "Ba",
    4: "Bốn",
    5: "Năm",
    6: "Sáu",
    7: "Bảy",
    8: "Tám",
    9: "Chín",
}


def num_to_text_less_than_1000(num: int) -> str:
    """
        Translate numbers that are between 0 and 999 into VND text format
    """
    global num_text

    # Extract the units, tens and hundreds from the number by getting the remainder
    # when divided by 10
    units = num % 10
    num //= 10

    tens = num % 10
    num //= 10

    hundreds = num % 10

    # The return text format
    ret = ""

    # Only add the translation text for units, tens and hundreds when it is greater than 0

    if hundreds > 0:
        ret += num_text[hundreds] + " Trăm "
    if tens > 0:
        # Special case: abc with b = 1, the translation will be different
        if tens == 1:
            ret += "Mười "
        else:  # abc, with b running from 2 to 9, read it normally
            ret += num_text[tens] + " Mươi "
    if units > 0:
        # Special case: abc, with b = 0 and a running from 1 to 9
        if tens == 0 and hundreds > 0:
            ret += "Lẻ "
        # Special case: abc, with c = 5 and b running from 1 to 9
        if units == 5 and tens > 0:
            ret += "Lăm "
        else:
            # Read it normally
            ret += num_text[units] + " "
    return ret


def num2text(num: int) -> str:
    """
    Translate a number into VND text format
    """

    global num_text

    suffixes = (
        "Đồng",
        "Ngàn",
        "Triệu",
        "Tỷ",
        "Ngàn",
        "Triệu",
        "Tỷ"
    )

    # A list that will hold separated groups of three
    # (as a number) from the original number
    parts = []
    # A clone to help making the parts
    clone = num

    # The idea is to split the number by groups of three
    # (from thousand to million, then billion, then thousand of billion, etc)
    # and we will deal with each group one at a time

    # Add all groups of three into the parts list
    while clone > 0:
        parts.append(clone % 1000)
        clone //= 1000

    # We want to translate from left to right, so reverse the parts order
    parts.reverse()

    # The return value
    ret = ""

    # Iterate through all the parts
    for index, part in enumerate(parts):

        # (special case) Check the billion part to see if it is zero
        # If it does, then add the "Tỷ" suffix for the billion part to ret

        # Without the next 2 lines, there will be no "Tỷ" suffix for number
        # that have the billion part equals to zero.
        # For example, if the number is 1,000,000,000,000 the translation
        # will be "Một Ngàn Đồng Chẵn" instead of "Một Ngàn Tỷ Đồng Chẵn"
        if index == len(parts) - 4 and part == 0:
            ret += "Tỷ "

        # Only translate the part that are greater than 0
        # and a special case where the thousand part is zero
        if part > 0 or index == len(parts) - 1:

            # Add the translated part and the corresponding suffix part to ret
            ret += num_to_text_less_than_1000(part) + \
                suffixes[len(parts) - 1 - index] + " "

    # If the original number can be divided by 10 then add "Chẵn" to it
    if num % 10 == 0:
        ret += "Chẵn"

    return ret


if __name__ == "__main__":
    test_cases = [
        100_100_100,
        100_111_100,
        9_860_100_100,
        345_134_156,
        124_194_342,
        112_000,
        112_000_000,
        112_000_000_000_000,
        112_010_000_000_000,
        112_110_000_000_000,
        112_111_000_000_000,
        111,
        102,
        156,
        205,
        25
    ]

    for test_case in test_cases:
        print(f'{test_case:,}')
        print(num2text(test_case))
        print()
