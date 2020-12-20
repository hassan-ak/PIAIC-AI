# Function for gross pay according to following rule.
# Gross Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
def grosspay(hours,rate_per_hour):
    if hours<=40:
        gross_pay = hours*rate_per_hour
        return gross_pay
    else:
        pay_1 = 40*rate_per_hour
        pay_2 = (hours-40)*rate_per_hour*1.5
        gross_pay = pay_1+pay_2
        return gross_pay
    
    
    
    
    
# Function for income tax where income tax is 4% of the gross pay
def incometax(hours,rate_per_hour,rate=4):
    income_tax = grosspay(hours,rate_per_hour) * (4 / 100)
    return income_tax





# Function for net pay
def netpay(hours,rate_per_hour,rate=4):
    net_pay = grosspay(hours,rate_per_hour) - incometax(hours,rate_per_hour,rate=4)
    return net_pay