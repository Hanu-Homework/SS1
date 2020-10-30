from collections import Counter
from tree import Tree


def read_as_string(file_name: str):
    try:
        with open(file_name, "r") as f:
            data = f.read()
    except OSError:
        return None
    else:
        return data


def write_compression_to_file(bits: str):
    binary_data = b''

    for bit in bits:
        if bit == '0':
            binary_data += b'0'
        else:
            binary_data += b'1'

    with open("test.bnr", "wb") as f:
        f.write(binary_data)


def main():
    string = read_as_string("example.txt")

    tree = Tree(Counter(list(string)).items())

    translated_map = tree.get_translated()

    for char, value in translated_map.items():
        if char == '\n':
            print(f"(\\n) {value}")
        else:
            print(f"({char}) {value}")

    compressed = ''

    for c in string:
        compressed += translated_map[c]

    print(f"Compressed: {compressed}")

    print(f"Size before compression: {len(string) * 8}")
    print(f"Size after compression: {len(compressed)}")

    compression_ratio = len(compressed) / (len(string) * 8)
    print(f"Compression ratio: {compression_ratio}")

    write_compression_to_file(compressed)


if __name__ == "__main__":
    main()