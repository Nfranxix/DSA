monthly_expenses = [2200,2350,2600,2130,2190]  # Reading from month of January to May 

def dollars_spent_extra(list):
    extra =monthly_expenses[1] - monthly_expenses[0]
    return extra

def expenses_in_first_quater(list):  # First Three months
    total = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
    return total

def comparison(list):
    for x in monthly_expenses:
        if x == 2200:
            return True
    return False

def add_element(list): # For the month of June 
    monthly_expenses.append(1980)

def refund_correction(list):  # Refund in the month of April
    monthly_expenses[3] = monthly_expenses[3] - 200
