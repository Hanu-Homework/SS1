def num2text(num: int) -> str:
    """
    Translate a number into VND text format
    """

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

    suffixes = [
        "Đồng",
        "Mươi",
        "Trăm",
        "Ngàn",
        "Mươi",
        "Trăm",
        "Triệu",
        "Mươi",
        "Trăm",
        "Tỷ",
        "Mươi",
        "Trăm",
        "Ngàn",
        "Mươi",
        "Trăm",
        "Triệu",
        "Tỷ",
    ]

    l = len(str(num))

    clone = num
    count = 0
    result = ""

    is_thousand_suffix_read = False

    while clone > 0:
        num_value = clone % 10

        if num_value == 0:
            count += 1
            clone //= 10
            continue

        suffix = count % len(suffixes)

        if suffix % 3 == 0:
            is_thousand_suffix_read = True
        else:
            is_thousand_suffix_read = False

        result = num_text[num_value] + " " + \
            suffixes[suffix] + " " + result

        count += 1
        clone //= 10

    if not is_thousand_suffix_read:
        result += suffixes[count - count % 3] + " "

    if num % 10 == 0:
        result += "Chẵn"

    return result


if __name__ == "__main__":
    num = int(input())
    print(f'{num:,}')
    result = num2text(num)
    print(result)
