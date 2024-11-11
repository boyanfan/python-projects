import numpy as np

# Given data
payments = [690, 790, 890, 990, 1090, 1190]
interest_rate_first_six_years = 0.10
interest_rate_subsequent_years = 0.07
total_years = 65
years_of_first_interest_rate = 6

# Calculate future value of each payment
future_value = 0

for i, payment in enumerate(payments):
    # Calculate the years the money will be invested with the second interest rate
    years_invested = total_years - (i + 1)
    # Calculate the future value for the first interest rate period
    value_after_first_period = payment * ((1 + interest_rate_first_six_years) ** years_of_first_interest_rate)
    # Calculate the future value after the second interest rate period
    future_value += value_after_first_period * ((1 + interest_rate_subsequent_years) ** (years_invested - years_of_first_interest_rate))

future_value = round(future_value, 2)

print(future_value)