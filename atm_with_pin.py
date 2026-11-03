print("Welcome, what is your account name?\n")

# tuple of dictionaries containing
# customer user and passcode, then total price and transaction history for each user
users = (
    {"Billy": 1235, "Transaction": ["ASUS ROG tablet"]},
    {"Darren": 4516, "Transaction": ["REDMAGIC Astra 2", "Adidas snapback", "Bape Cardigan"]},
    {"Sofia": 7819, "Transaction": ["iPhone duo (grey)"]},
    {"Ankara": 7261, "Transaction": ["PS5 bundle (FC 26)", "Fortnite Vbucks (250)", "Toad Water Bottle"]}
)

user = input("Account name: ")

# Find the customer's account
customer = next((cust for cust in users if user in cust), None)

if customer is None:
    print("User not found!")

else:
    remaining_attempts = 3

    while remaining_attempts > 0:
        pin_check = int(input("Enter your PIN: "))

        if pin_check == customer[user]:
            print(f"\nWelcome to your account, {user}!")

            # Unpack transaction history into a readable string
            transactions = "\n".join(customer["Transaction"])

            print(f"\nTransaction history:\n{transactions}")
            break

        remaining_attempts -= 1
        print(f"Wrong PIN! {remaining_attempts} attempts left.")

    else:
        print("Account is now locked.")
# how can i implement a transaction history?
# change to a list of dictionaries?? then implement name: key, transaction: history.. per name
# name and pin always stored in the first dict
# transaction history stored in the second item as value, key is just transaction title