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
    combined = {**defaults, **customer_info}
    return combined
"""print(create_customer(
    name="Henry",
    age=19,
    country="Poland",
    active=True
))"""

# 09 - CALCULATE AVERAGE SCORES
def average_scores(*scores):
    res = sum(scores)
    return res / len(scores)
#print(average_scores(1, 1, 1, 1, 1))

# 10 - SHOPPING BASKET
def basket_total(*prices):
    res = sum(prices)
    return res
#print(basket_total(20, 5, 5, 10))

# 11 - CALCULATE TOTAL REVENUE
def total_revenue(*sales):
    res = 0
    for x in sales:
        res += x
    return res
#print(total_revenue(10, 20, 30, 40, 50))

# 12 - FIND HIGHEST TRANSACTION
def largest_transaction(*transaction):
    return max(transaction)
#print(largest_transaction(220, 350, 400, 120, 55))

# 13 - SALES REPORT
def sales_report(*sales, **options):
    total = sum(sales) # initial sales total without tax

    # handling tax in options
    """if "tax" in options:
        total += (total * options["tax"])"""
    # instead of the above
    tax = options.get("tax", 0)
    total += total * options["tax"]

    avg = total / len(sales) # avergae total sales

    # handle currencies, providing currency code and associating with symbol
    currencies = {"GBP": "£",
                "USD": "$",
                "CAD": "$",
                "EUR": "€"}
    """if "currency" in options:
        if options["currency"] in currencies:
            currency = currencies[options["currency"]]"""
    # instead of the above

    currency = currencies[options.get("currency", "")]

    return f"Total: {currency}{total:.2f} \n Average: {currency}{avg:.2f}"
#print(sales_report(100, 100, tax=0.2, currency="USD"))

# - DATA SUMMARY FUNCTION
def summarise_data(*values, **options):
    min_request = options.get("minimum", False)
    max_request = options.get("maximum", False)
    avg_request = options.get("average", False)
    res = {}

    # gradually add to res if metric is needed
    # if options value is true, calculate metric
    if min_request:
        min_value = min(values)
        res["minimum"] = min_value
    if max_request:
        max_value = max(values)
        res["maximum"] = max_value
    if avg_request:
        avg_value = round(sum(values) / len(values), 2)
        res["average"] = avg_value

    # formatting for concise readability
    format_res = ""
    if len(res.items()) == 0:
        format_res = "No metrics requested currently."
    else:
        for key, value in res.items():
            format_res += f"{key}: {value}\n"

    return format_res

data_summary = summarise_data(5, 10, 20, minimum=True, maximum=False, average=False)
print(data_summary)
