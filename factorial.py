# Step 1:
# Create a function named factorial
# This function should take one number as input

# Step 2:
# Add a small description inside the function
# This is called a docstring
# It tells what the function does

# Step 3:
# Check the base condition
# If the number is 0 or 1,
# return 1
# because factorial of 0 and 1 is always 1

# Step 4:
# Otherwise, use recursion
# Multiply the number by factorial of (number - 1)

# Step 5:
# This means the function will keep calling itself
# until it reaches 1 or 0


# Step 6:
# Print the docstring of the function

# Step 7:
# Print the factorial of 0

# Step 8:
# Print the factorial of 1

# Step 9:
# Print the factorial of 2

# Step 10:
# Print the factorial of 5

# Step 11:
# Print the factorial of 10
def factorial(x):
    """ It will multiply by factorial of number"""
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print(factorial(3))