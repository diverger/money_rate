# -*- coding: GB2312 -*-
# https://www.python.org/dev/peps/pep-0263/
# http://stackoverflow.com/questions/14472650/python-3-encode-decode-vs-bytes-str
# http://pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
# http://stackoverflow.com/questions/8258432/days-between-two-dates-in-python
# http://stackoverflow.com/questions/19157374/python-input-validation
# http://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e-in-python
# 我想在定期存款到期前转存为其他产品，我会赚还是会赔呢？算一算吧
from datetime import date
from datetime import datetime, timedelta

def get_input_date(prompt):
    try:
        s = input(prompt)
        d = datetime.strptime(s, "%Y.%m.%d")
        return d
    except ValueError as e:
        print ("Please enter a valid date as " + str(e))
        return None

def get_input_value(prompt):
    try:
        s = input(prompt)
        v = float(s)
        return v
    except ValueError as e:
        print ("Please enter a valid number as " + str(e))
        return None

str_prompt = "Input principal:"
principal = get_input_value(str_prompt)
while not isinstance(principal,float) or principal < 0:
    principal = get_input_value(str_prompt)

str_prompt = "Input annual interest rate in % ( = day X 360, = month X 12 ):"
annual_interest_rate = get_input_value(str_prompt)
while not isinstance(annual_interest_rate, float) or annual_interest_rate < 0:
    annual_interest_rate = get_input_value(str_prompt)

str_prompt = "Input start date (XXXX.XX.XX):"
start_date = get_input_date(str_prompt)
while not isinstance(start_date, datetime):
    start_date = get_input_date(str_prompt)

str_prompt = "Input end date (XXXX.XX.XX):"
end_date = get_input_date(str_prompt)
while not isinstance(end_date, datetime):
    end_date = get_input_date(str_prompt)

time_delta = end_date - start_date
ds = time_delta.days
print("Total {0} days".format(ds))

profit = annual_interest_rate / 360 / 100 * ds * principal

print("Total profit: {}".format(profit))
