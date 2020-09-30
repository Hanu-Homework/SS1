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
    global num_text

    don_vi = num % 10
    num //= 10

    chuc = num % 10
    num //= 10

    tram = num % 10

    ret = ""
    if tram > 0:
        ret += num_text[tram] + " Trăm "
    if chuc > 0:
        if chuc == 1:
            ret += "Mười "
        else:
            ret += num_text[chuc] + " Mươi "
    if don_vi > 0:
        ret += num_text[don_vi] + " "
    return ret


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

    suffixes = (
        "Đồng",
        "Ngàn",
        "Triệu",
        "Tỷ",
        "Ngàn",
        "Triệu",
        "Tỷ"
    )

    parts = []
    clone = num

    while clone > 0:
        parts.append(clone % 1000)
        clone //= 1000

    parts.reverse()

    ret = ""

    for index, part in enumerate(parts):

        ret += num_to_text_less_than_1000(part) + \
            suffixes[len(parts) - 1 - index] + " "

    if num % 10 == 0:
        ret += "Chẵn"

    return ret


if __name__ == "__main__":
    test_cases = [
        100_100_100,
        100_111_100,
        9_860_100_100,
        345_134_156,
        124_194_342
    ]

    for test_case in test_cases:
        print(f'{test_case:,}')
        print(num2text(test_case))
        print()
