from file_handler import view_file, add_to_file, update_file


def main():
    file_path = input("Enter the relative file path: ")

    while True:
        print("\n--- Document Word Count Updater ---")
        print("1. Update document info")
        print("2. View document")
        print("3. Add content") 
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            update_file(file_path)

        elif choice == "2":
            view_file(file_path)

        elif choice == "3":
            add_to_file(file_path)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()