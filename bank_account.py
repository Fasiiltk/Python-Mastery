# bank_account.py
balance = 0

while True: 
    print(f"\nBalance: ${balance}")
    print("1. Deposit\n2. Withdraw\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = float(input("Enter amount: "))
        balance += amount
    elif choice == "2":
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds!")
    elif choice == "3":
        break
    else:
        print("Invalid choice")
