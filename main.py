def candidate_login():
    print("\n--- Candidate Login ---")

    username = input("Enter candidate username: ")
    password = input("Enter password: ")

    if username == "candidate" and password == "1234":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


def show_exam_instructions():
    print("\n--- Exam Instructions ---")
    print("1. Read each question carefully.")
    print("2. Choose one answer for each question.")
    print("3. Each correct answer carries 1 mark.")
    print("4. No negative marking.")


def conduct_exam():
    print("\n--- Online Exam ---")

    questions = [
        {
            "question": "Which language is used for this project?",
            "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
            "answer": "B"
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["A. int", "B. str", "C. bool", "D. list"],
            "answer": "C"
        },
        {
            "question": "Which keyword defines a function in Python?",
            "options": ["A. function", "B. define", "C. fun", "D. def"],
            "answer": "D"
        }
    ]

    score = 0

    for question in questions:
        print("\n" + question["question"])

        for option in question["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == question["answer"]:
            score += 1

    print("\n--- Exam Result ---")
    print(f"Your score: {score}/{len(questions)}")


def main():
    print("Online Examination System")
    print("Welcome to the Examination Portal")

    if candidate_login():
        show_exam_instructions()

        start_exam = input("\nDo you want to start the exam? (yes/no): ")

        if start_exam.strip().lower() == "yes":
            conduct_exam()
        else:
            print("Exam not started.")


if __name__ == "__main__":
    main()