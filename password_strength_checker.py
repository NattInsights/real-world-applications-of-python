print("PASSWORD STRENGTH CHECKER")
password = input("Enter a password: ")
digits = [0,10]
symbols = "!'£$%^&*()-=+/?#~@"

rating = 3
if len(password) <= 8:
    rating -= 1
if digits not in password:
    rating -= 1
