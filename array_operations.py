# 1) Import the `array` module:
#    a) Use alias `arr` for easier reference.

# 2) Create an array `array_num`:
#    a) Use type code 'i' (integer type).
#    b) Initialize it with values [1, 3, 5, 3, 7, 9, 3].

# 3) Print the original array:
#    a) Convert the array into string using `str()`.
#    b) Display it with a message "Original array:".

# 4) Count occurrences of an element:
#    a) Use `count()` method to find how many times 3 appears.
#    b) Convert result to string and print with a proper message.

# 5) Reverse the array:
#    a) Use `reverse()` method to reverse elements in place.

# 6) Print the reversed array:
#    a) Display a heading message.
#    b) Convert array to string and print the result.


import array as x
array_num=x.array("i",[1,3,5,7,9,3])
print("Original Array"+ str(array_num))
print("Number of occurrences of the number 3 in the said array" + str(array_num.count(3)))
array_num.reverse()
print("Reverse order of the items: ")
print(str(array_num))