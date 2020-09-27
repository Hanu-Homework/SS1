def order_linear_search(item: object, array: list) -> bool:
    # Iterate through each element in the array
    for element in array:
        # If the element is equal to the item
        if item == element:
            # Break the loop right away and return true
            return True
    # The loop has finished and no element in the array is equal to the item, thus, return false
    return False


if __name__ == '__main__':
    items = input("Enter the elements in one line, separated by a space: ").split(" ")

    to_search = input("Enter the element to search: ")

    result = order_linear_search(to_search, items)

    print(f"Result: {result}")
