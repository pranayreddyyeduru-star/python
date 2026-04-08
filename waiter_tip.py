# Step 1:
# Make a function named total_calc
# This function should take 2 inputs:
# 1. bill_amount  → the restaurant bill
# 2. tip_perc     → the tip percentage


# Step 2:
# Find the total amount after adding tip
# Formula idea:
# total = bill + tip
# tip = bill_amount * tip_perc / 100


# Step 3:
# Round the total to 2 decimal places
# because money is usually written like 150.00


# Step 4:
# Show the final amount the person has to pay
# Example output:
# Please pay $180.0


# Step 5:
# Call the function with:
# bill = 150
# tip = 20%
def total_calc(bill_amount, tip_perc):
    tip = bill_amount * tip_perc / 100
    total = bill_amount + tip
    float(total)
    print(total)
total_calc(150,20)
