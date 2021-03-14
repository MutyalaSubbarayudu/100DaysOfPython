print("Welcome to Tip Calculator")

total_bill = float( input("What was the total bill? $") )
tip_percentage = int( input("What percentage of tip would you like to give? 10, 12, or 15? ") )
number_of_people = int( input("How many people to split the bill? ") )

total_bill += total_bill * ( tip_percentage / 100 )

# individual_bill_amount = round( total_bill / number_of_people , 2 )

individual_bill_amount = total_bill/number_of_people

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
individual_bill_amount = "{:.2f}".format(individual_bill_amount)

print(f"Each person should pay: ${ individual_bill_amount }")