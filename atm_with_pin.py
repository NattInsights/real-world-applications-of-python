print("Welcome, what is your account name?\n")

users = {
    "Billy": 1235,
    "Darren": 4516,
    "Sofia": 7819,
    "Ankara": 7261
}

user = input()
if user not in users:
    print("User not found!")
else:
    pin_check = int(input("Enter your pin: "))
    remaining_attempts = 2
    while remaining_attempts > 0:
        if pin_check != users[user]:
            print(f"Wrong pin, please try again\n {remaining_attempts} attempts left.")
            remaining_attempts -= 1
            pin_check = int(input())
        elif pin_check == users[user]:
            print(f"Welcome to your account {user}!!")
            break
if remaining_attempts == 0:
    print("Account is now locked.")
# how can i implement a transaction history?
# change to a list of dictionaries?? then implement name: key, transaction: history.. per name
# name and pin always stored in the first dict
# transaction history stored in the second item as value, key is just transaction title