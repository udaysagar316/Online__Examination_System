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


def main():
    print("Online Examination System")
    print("Welcome to the Examination Portal")

    candidate_login()


if __name__ == "__main__":
    main()