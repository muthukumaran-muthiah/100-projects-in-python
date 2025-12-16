print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_people = int(input("How many people to split the bill?"))
total_bill = ((tip / 100) * bill) + bill
share = (total_bill / number_of_people)
final_amount = round(total_bill, 2)
print(f"Each person should pay: {final_amount}")
