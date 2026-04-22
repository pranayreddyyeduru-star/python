# 3) Define a function `getRandomDate(startDate, endDate)`:

# (This function generates a random date between the given start 
# and end dates.)

# 4) Inside the function, print a message showing the start and end 
# date range.

# 5) Generate a random decimal number between 0 and 1 using `random.random()`

# and store it in `randomGenerator`.

# 6) Set the date format string `dateFormat = '%m/%d/%Y'`

# to match the input dates (month/day/year).

# 7) Convert the start date string into epoch time (seconds):

# a) Convert `startDate` to a time structure using
#  `time.strptime(startDate, dateFormat)`.

# b) Convert it to seconds using `time.mktime(...)`.

# c) Store it in `startTime`.

# 8) Convert the end date string into epoch time (seconds) the same way

# and store it in `endTime`.

# 9) Generate a random time value between `startTime` and `endTime`:

# a) Compute
#  `randomTime = startTime + randomGenerator * (endTime - startTime)`.

# 10) Convert `randomTime` back into a formatted date string:

# a) Convert to local time using `time.localtime(randomTime)`.

# b) Format it as a date string using `time.strftime(dateFormat, ...)`.

# c) Store it in `randomDate`.

# 11) Return the generated random date string `randomDate`.

# 12) Call the function with "1/1/2016" and "12/12/2018"

# and print the returned random date as the final output.
import random
import time
def RandomDate(startDate, endDate):
    print(f"The start date and end date range is {startDate} and {endDate}")
    randomGenerator=random.random()
    dateFormat = '%m/%d/%Y'
    startTime=time.mktime(time.strptime(startDate, dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))
    randomTime= startTime + randomGenerator * (endTime - startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print(RandomDate("1/1/2016", "12/12/2018"))