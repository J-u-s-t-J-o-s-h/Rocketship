#!/usr/bin/env python3

def prompt_user(questions):
    answers = {}
    for question in questions:
        answer = input(question + ": ")
        answers[question] = answer
    return answers


def save_answers_to_file(filename, answers):
    with open(filename, 'a') as file:  # 'a' mode appends to the file
        for question, answer in answers.items():
            file.write(f"{question}: {answer}\n")
        file.write("\n")  # Add a newline to separate entries


def main():
    questions = [
        "Part Name: ",
        "Group #: ",
        "Part #: ",
        "Notes: "
    ]

    filename = "user_answers.txt"

    while True:
        answers = prompt_user(questions)
        save_answers_to_file(filename, answers)
        print(f"Answers have been saved to {filename}")

        cont = input("Do you want to add more information? (yes/no): ").strip().lower()
        if cont != 'yes':
            break


if __name__ == "__main__":
    main()
