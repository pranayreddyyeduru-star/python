# 1) Create a boolean variable `valid = False`.
#    (This will be used to keep asking for input until a valid number is entered.)

# 2) Start a `while not valid` loop so the program repeats until `valid` becomes True.

# 3) Inside the loop, use a `try` block to handle invalid (non-integer) input safely.

# 4) Ask the user to enter a number and convert it to an integer:
#    a) Store the input in `n` using `n = int(input(...))`.

# 5) Use another `while` loop to check if the number is even:
#    a) Repeat while `n % 2 == 0` (meaning `n` is divisible by 2).
#    b) Print "bye" inside the loop.
#    (This loop will keep running as long as `n` stays even.)

# 6) After the inner loop ends, set `valid = True`
#    so the outer loop stops repeating.

# 7) If the user enters something that is not a number,
#    a `ValueError` occurs and the `except` block runs:
#    a) Print "Invalid"
#    b) The outer loop continues and asks again.
valid=False
while not valid:
    try:
        n=int(input("Give me a number: "))
        while n%2==0:
            print("bye")
        valid=True
    except ValueError:
        print("Invalid")
