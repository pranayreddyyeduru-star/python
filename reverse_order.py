#Write a program to print the numbers in reverse order beginning from the
#  number entered by the user.

# 1) Ask the user to enter a number (greater than 1) and store it in `n`.

# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases 
# by 1 each time.

# 4) Inside the loop, print the current value of `i`
#  (so numbers appear in reverse order).

n=int(input("Give me a number greater than 1: "))
print("I will print the numbers fron n down to 1")
for i in range(n,1,-1):
    print(i)