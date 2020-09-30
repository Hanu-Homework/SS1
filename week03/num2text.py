def num2text(num: int) -> str:
    """
    """

    trans = {
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

    currency = [
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

    cache = num
    count = 0
    ret = ""

    flag = False

    while cache > 0:
        to_read1 = cache % 10

        if to_read1 == 0:
            count += 1
            cache //= 10
            continue

        to_read2 = count % len(currency)

        if to_read2 % 3 == 0:
            flag = True
        else:
            flag = False

        ret = trans[to_read1] + " " + \
            currency[to_read2] + " " + ret

        count += 1
        cache //= 10

    if not flag:
        ret += currency[count - count % 3] + " "

    if num % 10 == 0:
        ret += "Chẵn"

    return ret


if __name__ == "__main__":
    num = int(input())
    print(f'{num:,}')
    result = num2text(num)
    print(result)
