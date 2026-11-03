print("Welcome, what is your account name?\n")

# tuple of dictionaries containing
# customer user and passcode, then total price and transaction history for each user
users = (
    {"Billy": 1235, "Transaction": ["ASUS ROG tablet"]},
    {"Darren": 4516, "Transaction": ["REDMAGIC astra 2", "Adidas snapback", "Bape Cardigan"]},
    {"Sofia": 7819, "Transaction": ["iPhone duo (grey)"]},
    {"Ankara": 7261, "Transaction": ["PS5 bundle (fc 26)", "Fornite Vbucks (250)", "Toad Water Bottle"]}
)

user = input()
remaining_attempts = 3
for cust in users:
    if user not in cust.keys():
        print("User not found!")
        break
    else:
        pin_check = int(input("Enter your pin: "))
        remaining_attempts = 2
        while remaining_attempts > 0:
            if pin_check != cust[user]:
                print(f"Wrong pin, please try again\n {remaining_attempts} attempts left.")
                remaining_attempts -= 1
                pin_check = int(input())
            elif pin_check == cust[user]:
                print(f"Welcome to your account {user}!!")
                print(f"Transaction history:\n" + str(cust["Transaction"]))
                break
    if remaining_attempts == 0:
        print("Account is now locked.")
# how can i implement a transaction history?
# change to a list of dictionaries?? then implement name: key, transaction: history.. per name
# name and pin always stored in the first dict
# transaction history stored in the second item as value, key is just transaction title