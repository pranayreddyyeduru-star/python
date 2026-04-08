# Step 1:
# Create a function named cube
# This function should take one number as input

# Step 2:
# Inside the function, return the cube of the number
# Cube means:
# number × number × number


# Step 3:
# Create another function named by_three
# This function should also take one number as input


# Step 4:
# Check if the number is divisible by 3
# Hint:
# Use modulo (%) operator
# If remainder is 0, it means divisible by 3


# Step 5:
# If the number is divisible by 3,
# call the cube() function and return its result


# Step 6:
# If the number is NOT divisible by 3,
# return False


# Step 7:
# Display the result for:
# 9
# 4
def cube(x):
    return x*x*x
def by_three(x):
    if x%3==0:
        return cube(x)
    else:
        return False
print(by_three(9))
print(by_three(4))