##############################################
# Tip Calculator
# Purpose: Calculate tips based on total Bill
# Author: AJ
#############################################

print("Welcome to the Tip Calculator")
print()

# Get user input needed to calculate tip
bill = input("What was the total Bill?: ")
tip_percentage = input("What percentage would you like "
                       "to Tip 10, 12, or 15? :")
bill_sharing = input("How many people are sharing the Bill? :")

# Convert string to number for calculation
bill_input = float(bill)
tip_input = int(tip_percentage)
bill_sharing_input = int(bill_sharing)

# Forumla for calculating Tip
tip_calculated = bill_input * (100 + tip_input) / 100

# Total to tip based on those sharing
total_to_tip = round (tip_calculated, 2) / bill_sharing_input

print()
print(f"Total Bill: ${bill_input}")
print(f"Amount to tip: {tip_input}%")
print(f"Total Splitting Bill: {bill_sharing_input}")
print(f"Each person should pay: ${total_to_tip}")

