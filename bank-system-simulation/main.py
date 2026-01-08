from bank import Bank


def print_menu() -> None:
    print("\n=== BANK SYSTEM ===")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View account")
    print("5. Exit")


def create_account(bank: Bank) -> None:
    owner = input("Enter full name: ").strip()
    account_type = input("Account type (savings/current): ").strip().lower()

    try:
        account_number = bank.create_account(owner, account_type)
        print(f"Account created successfully. Account Number: {account_number}")
    except ValueError as e:
        print(f"Error: {e}")


def deposit(bank: Bank) -> None:
    try:
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_number, amount)
        print("Deposit successful.")
    except Exception as e:
        print(f"Error: {e}")


def withdraw(bank: Bank) -> None:
    try:
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(account_number, amount)
        print("Withdrawal successful.")
    except Exception as e:
        print(f"Error: {e}")


def view_account(bank: Bank) -> None:
    try:
        account_number = int(input("Enter account number: "))
        account = bank.get_account(account_number)

        print("\n--- Account Details ---")
        print(f"Account Number: {account['account_number']}")
        print(f"Owner: {account['owner']}")
        print(f"Type: {account['type']}")
        print(f"Balance: {account['balance']}")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    bank = Bank()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            create_account(bank)
        elif choice == "2":
            deposit(bank)
        elif choice == "3":
            withdraw(bank)
        elif choice == "4":
            view_account(bank)
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 5.")


if __name__ == "__main__":
    main()