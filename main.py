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


def main():
    print("Online Examination System")
    print("Welcome to the Examination Portal")

    if candidate_login():
        show_exam_instructions()


if __name__ == "__main__":
    main()