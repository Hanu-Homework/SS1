def clean_up(string: str) -> str:
    return string.strip()


if __name__ == "__main__":

    try:
        with open("example_driver_license_exam.txt", "r") as f:
            # Read all the lines from the txt file
            # Each line will be the candidate answer,
            # line number will also be the question number
            candidate_answers = list(map(clean_up, f.readlines()))

        with open("example_driver_license_answer.txt", "r") as f:
            correct_answers = list(map(clean_up, f.readlines()))

    except OSError as e:
        print(e)

    # Ensure that the length of the candidate answer is exactly 20
    assert len(candidate_answers) == len(correct_answers)

    # A value that will hold the number of correct answers
    correct_count = 0

    # A value that will hold the number of wrong answers
    wrong_count = 0

    # A list that will contain the indexes for the wrong answered questions
    wrong_answer_indexes = []

    # Iterate through all the answers
    for index, (candidate_answer, correct_answer) in enumerate(zip(candidate_answers, correct_answers)):

        # If the answer is correct
        if candidate_answer == correct_answer:
            # Increase the correct counter by 1
            correct_count += 1
        else:  # Else, the answer is incorrect
            # Then increase the wrong counter by 1
            wrong_count += 1
            # And add the question number to the wrong list
            wrong_answer_indexes.append(index + 1)

    # Print out the result
    print(f"Number of correct answers: {correct_count}/20")
    print(f"Number of wrong answers: {wrong_count}/20")
    print(f"Wrong answers: {wrong_answer_indexes}")
