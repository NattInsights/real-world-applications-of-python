def finance(monthly_income):
    # essentials rn can be driving for me
    essentials = monthly_income * 0.55
    guilt_free = monthly_income * 0.05
    investing = monthly_income * 0.1
    short_term_goal = monthly_income * 0.15
    saving = monthly_income * 0.15

    return f"""Essentials: {essentials}
        Guilt-free: {guilt_free}
        Investing: {investing}
        Short term: {short_term_goal}
        Investing: {saving}
        """
print(finance(2005))