def formatted(date_str: str) -> str:

    # Split the month, day and year from the string
    month, day, year = map(int, date_str.split("/"))

    # A translator to convert the numeric month to a named one
    month_translator = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    # return the formatted version
    return f"{month_translator[month]} {day}, {year}"


if __name__ == "__main__":

    # Get the input date string from the user
    date_string = input("Enter the date string: ")

    # Convert the given date string into a formatted version
    result_python = formatted(date_string)

    # Print out the result
    print(f"Result: {result_python}")
