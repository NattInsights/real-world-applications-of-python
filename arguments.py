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
# print(net_salary(28000))

# 04 - CUSTOMER GREETING
def greet_customer(name, greeting="Hello"):
    return greeting, name
# print(greet_customer("Elisa"))

# 05 - PRODUCT INFORMATION
def product_info(name, price, category="General"):
    return name + " | " + price + " | " + category
# print(product_info("Iphone 18 pro max", "1,400", "Electronics"))

# 06 - EMPLOYEE RECORD
def employee(**info):
    return info
"""print(employee(
    name="Luukas",
    department="Data Science",
    salary=60000
))"""

# 07 - SALES TRANSACTION
def sale(product, price, quantity=1, discount=0):
    final_transaction = price - (price * discount) * quantity
    return f"{product}: \nTotal amount - £{final_transaction:.2f}"
"""print(sale(
    product="Asus Zenbook A14",
    price=899,
    discount=0.30
    ))"""

# 08 - CUSTOMER ACCOUNT
def create_customer(country="UK", active=True, **customer_info):
    defaults = {"Country": country, "Active": active}
    combined = {**defaults, customer_info}
    return combined
print(create_customer(
    name="Levy",
    age=32,
))
# still working on piecing together the kwargs and regular default arguments
# attempting to make them a dictionary and return it altogther

