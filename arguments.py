# 01 - TOTAL PRICE
def calculate_total(price, quantity):
    return price * quantity
# print(calculate_total(15, 4))

# 02 - PRICE WITH DISCOUNT
def calculate_discount(price, discount=0.10):
    return price - (price * discount)
# print(calculate_discount(100))
# print(calculate_discount(100, 0.35))

# 03 - SALARY AFTER TAX
def net_salary(salary, tax_rate=0.2):
    return salary - (salary * tax_rate)
print(net_salary(28000))

