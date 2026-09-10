def main():
    while True:
        print("*********************************")
        print("    PERSONAL FINANCE MANAGER")
        print("*********************************")
        print()
        print("1. Add income")
        print("2. Add expense")
        print("3. Show balance")
        print("4. Show transactions")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("You selected: Add income")
        elif choice == "2":
            print("You selected: Add expense")
        elif choice == "3":
            print("You selected: Show balance")
        elif choice == "4":
            print("You selected: Show transaction")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please, choose 1-5.")

if __name__ == "__main__":
    main()