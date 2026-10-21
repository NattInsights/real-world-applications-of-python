balance = 1000

print("=== MENU ===")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")

choice = input("Choose an option (1, 2, or 3): ")

check_balance = choice == "1"
deposit = choice == "2"
withdraw = choice == "3"

final_output = ""

if check_balance:
    final_output += f"Total balance: {balance}\n"

if withdraw:
    withdraw_amount = int(input("Enter an amount to withdraw: "))
    if balance >= withdraw_amount:
        final_output += f"{withdraw_amount} successfully withdrawn\n"
        balance -= withdraw_amount
    else:
        final_output += "Withdraw amount exceeds balance\n"

if deposit:
    deposit_amount = int(input("Enter an amount to deposit: "))
    balance += deposit_amount
    final_output += f"{deposit_amount} successfully deposited\n"

print(final_output)
print(f"Updated balance: {balance}")



