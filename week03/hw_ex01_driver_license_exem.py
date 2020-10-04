if __name__ == "__main__":
    correct_answers = "ACAADBCACBADCADCBBDA"

    with open("example_driver_license_exam.txt", "r") as f:
        lines = f.readlines()

        assert len(lines) == 20
        assert len(lines) == len(correct_answers)

        correct_count = 0
        wrong_count = 0

        wrong_answer_indexes = []

        for index, (line, correct_answer) in enumerate(zip(lines, correct_answers)):
            candidate_answer = line.strip()

            if candidate_answer == correct_answer:
                correct_count += 1
            else:
                wrong_count += 1
                wrong_answer_indexes.append(index + 1)

        print(f"Number of correct answers: {correct_count}/20")
        print(f"Number of wrong answers: {wrong_count}/20")
        print(f"Wrong answers: {wrong_answer_indexes}")
