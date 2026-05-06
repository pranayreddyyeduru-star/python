# 1) Create two sets:
#    a) `setx` containing elements "green" and "blue".
#    b) `sety` containing elements "blue" and "yellow".

# 2) Print a heading message:
#    a) "Original set elements:"

# 3) Print both sets:
#    a) Print `setx`.
#    b) Print `sety`.

# 4) Print a newline and heading:
#    a) "\nIntersection of two said sets:"

# 5) Perform intersection operation:
#    a) Use `intersection()` method.
#    b) It returns only common elements from both sets.
#    c) Store the result in `setz`.

# 6) Print the resulting set `setz`:
#    a) Output will contain elements common in both sets.
setx={"green", "blue"}
sety={"blue", "yellow"}
print(f"Original set elements:{setx}and {sety}")
print("\nIntersection of two said sets:")
setz=setx&sety.intersection()
print(setz)