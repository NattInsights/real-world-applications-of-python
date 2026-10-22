print("PASSWORD STRENGTH CHECKER")
password = input("Enter a password: ")
# digits = range(0, 10) - no digit variable needed with isdigit
symbols = "!'£$%^&*()-=+/?#~@"

rating = 0

# length checks
if len(password) >= 8:
    rating += 1

# digit checks
if any(char.isdigit for char in password):
    rating += 1

# symbols checks     
if any(char in symbols for char in password):
   rating += 1 

# uppercase checks
if any(char.isupper() for char in password):
    rating += 1

# strength config
if rating <= 1:
    strength = "Weak"
elif rating == 2 or rating == 3:
    strength = "Medium"
elif rating == 4:
    strength = "Strong"

print(f"Password strength: {strength}")
