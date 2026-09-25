import random
from datetime import datetime

accounts = {}


def generate_account_number():
    while True:
        account_number = str(random.randint(10000000, 99999999))
        if account_number not in accounts:
            return account_number


def create_account():
    print("\n--- Create Account ---")

    name = input("Enter your name: ").strip()
    phone = input("Enter phone number: ").strip()
    pin = input("Create a 4-digit PIN: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if not phone.isdigit():
        print("Please enter a valid phone number.")
        return

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number is:", account_number)
    print("Please keep your account number and PIN safe.")


def login():
    print("\n--- Login ---")

    account_number = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    account = accounts.get(account_number)

    if account and account["pin"] == pin:
        print(f"\nWelcome, {account['name']}!")
        account_menu(account_number)
    else:
        print("Invalid account number or PIN.")


def add_transaction(account, transaction_type, amount, details=""):
    time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    transaction = {
        "time": time,
        "type": transaction_type,
        "amount": amount,
        "details": details
    }

    account["transactions"].append(transaction)


def check_balance(account_number):
    account = accounts[account_number]

    print(f"\nCurrent Balance: ₹{account['balance']:.2f}")


def deposit(account_number):
    account = accounts[account_number]

    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    account["balance"] += amount

    add_transaction(account, "Deposit", amount)

    print(f"₹{amount:.2f} deposited successfully.")
    print(f"New Balance: ₹{account['balance']:.2f}")


def withdraw(account_number):
    account = accounts[account_number]

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount

    add_transaction(account, "Withdrawal", amount)

    print(f"₹{amount:.2f} withdrawn successfully.")
    print(f"Remaining Balance: ₹{account['balance']:.2f}")


def transfer_money(account_number):
    sender = accounts[account_number]

    receiver_number = input("Enter receiver account number: ").strip()

    if receiver_number not in accounts:
        print("Receiver account not found.")
        return

    if receiver_number == account_number:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > sender["balance"]:
        print("Insufficient balance.")
        return

    receiver = accounts[receiver_number]

    sender["balance"] -= amount
    receiver["balance"] += amount

    add_transaction(
        sender,
        "Transfer",
        amount,
        f"Sent to account {receiver_number}"
    )

    add_transaction(
        receiver,
        "Transfer",
        amount,
        f"Received from account {account_number}"
    )

    print(f"₹{amount:.2f} transferred successfully.")
    print(f"New Balance: ₹{sender['balance']:.2f}")


def transaction_history(account_number):
    account = accounts[account_number]

    print("\n--- Transaction History ---")

    if not account["transactions"]:
        print("No transactions found.")
        return

    for number, transaction in enumerate(account["transactions"], start=1):
        print(
            f"{number}. {transaction['time']} | "
            f"{transaction['type']} | "
            f"₹{transaction['amount']:.2f} | "
            f"{transaction['details']}"
        )


def change_pin(account_number):
    account = accounts[account_number]

    old_pin = input("Enter old PIN: ").strip()

    if old_pin != account["pin"]:
        print("Incorrect old PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    confirm_pin = input("Confirm new PIN: ").strip()

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    account["pin"] = new_pin

    print("PIN changed successfully.")


def account_menu(account_number):
    while True:
        print("\n========== ACCOUNT MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("==================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            transfer_money(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            change_pin(account_number)

        elif choice == "7":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n========== BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Thank you for using the Banking System.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
