print("""**TEMPERATURE AND UNIT CONVERTOR**
    1. Temperature convertor (Celscius/Fahrenheit)
    2. Distance metrics convertor (km/miles)
    3. Weight convertor (kg/lbs)""")
choice = int(input("Pick a convertor: "))

convert_temp = choice == 1
convert_distance = choice == 2
convert_weight = choice == 3
final = ""
# temp config
if convert_temp:
    amount = float(input("Enter amount: "))
    temp = input("Degrees (D) or Fahrenheit (F): ")
    check = temp.lower()
    if check == "degrees" or check =="d":
        degrees_converted = round((amount * 1.8) + 32, 2)
        final = f"{amount}C = {degrees_converted}F"
    elif check == "fahrenheit" or check == "f":
        fah_converted = round((amount - 32) / 1.8, 2)
        final = f"{amount}F = {fah_converted}C"
    else:
        "PLEASE ENTER A VALID OPTION AND AMOUNT"

# distance conversion
if convert_distance:
    amount = float(input("Enter an amount: "))
    dist = input("Is the amount in km or miles: ")
    check = dist.lower()
    if check == "km" or check == "kilo%":
        km_converted = round(amount * 0.6214, 2)
        final = f"{amount} km = {km_converted} miles"
    elif check == "miles":
        miles_converted = round(amount / 0.6241, 2)
        final = f"{amount} miles = {miles_converted} km"
    else:
        print("PlEASE ENTER A VALID OPTION AND AMOUNT")

# weight convertor
if convert_weight:
    amount = float(input("Enter an amount: "))
    weight = input("Is the amount in kg or lbs: ")
    check = weight.lower()
    if check == "kg" or check == "kilograms":
        kg_converted = round(amount * 2.205, 2)
        final = f"{amount}kg = {kg_converted}lbs"
    elif check == "lbs" or check == "pounds":
        lbs_converted = round(amount / 2.205, 2)
        final = f"{amount} miles = {lbs_converted}km"
    else:
        print("PlEASE ENTER A VALID OPTION AND AMOUNT")

print(final)