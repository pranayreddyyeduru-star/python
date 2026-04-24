# 1) Define a function `match_words(words)` that takes a list of words
#  as input.

# 2) Inside the function, initialize:

# a) `ctr = 0` to count how many words match the condition.

# b) `lst = []` to store the words whose first and last characters are the same.

# 3) Use a `for` loop to iterate through each `word` in the input list
#  `words`.

# 4) For each word, check the condition:

# a) The length of the word should be greater than 1 (`len(word) > 1`).

# b) The first character `word[0]` should be equal to the 
# last character `word[-1]`.

# 5) If the condition is true:

# a) Increase the counter `ctr` by 1.

# b) Add the word to the list `lst` using `lst.append(word)`.

# 6) After checking all words, print the list of matching words.

# 7) Return the final count `ctr`.

# 8) Call the function `match_words(...)` with a sample list of words

# and store the returned value in `count`.

# 9) Print the total number of words whose first and 
# last characters are the same.
def match_words(words):
    ctr = 0
    lst = []
    for i in words:
        if len(i) > 1 and i[0]==i[-1]:
            ctr+=1
            lst.append(i)
    print("List of words with first counter same\n", lst)
    return 
count=match_words(["abc", "cfc", "xyz", "aba", "1221"])
print("Number of words having first and last character same:", count)