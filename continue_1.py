# Step 1: Create a variable and assign it an initial value (for example 10)
# This variable will be used to control how many times the loop runs

# Step 2: Use a while loop that keeps running as long as the variable value is
#  greater than 0
# This means the loop will continue until the value becomes 0

# Step 3: Inside the loop, decrease the value of the variable by 1 in every
#  iteration
# This helps in gradually reaching the stopping condition of the loop

# Step 4: After decreasing the value, check if the current value becomes
#  equal to 5
# This is a special condition where we want different behavior

# Step 5: If the value is equal to 5, use the continue statement
# The continue statement skips the remaining part of the loop for that
#  iteration
# So, no output will be printed when the value is 5

# Step 6: If the value is not equal to 5, print the current value of the
#  variable
# This will display all values except the skipped one

# Step 7: The loop repeats these steps (decreasing, checking, printing)
# until the variable value becomes 0 and the loop condition becomes false

# Step 8: Once the loop finishes execution, print a final message like
#  "Good bye!"
# This indicates that the program has ended successfully
a=10
while a>0:
    a-=1
    if a==5:
        continue
    print(a)
print("Good Bye")