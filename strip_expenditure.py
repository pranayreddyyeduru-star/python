# 1) Define a function `hotel_cost(nights)` 
# that calculates hotel charges:

# a) Multiply 140 by the number of nights.

# b) Return the total hotel cost.

# 2) Define a function `plane_ride_cost(city)` that returns 
# airfare based on the city:

# a) If city is "Charlotte", return 183.

# b) Else if city is "Tampa", return 220.

# c) Else if city is "Pittsburgh", return 222.

# d) Else if city is "Los Angeles", return 475.

# 3) Define a function `rental_car_cost(days)` 
# that calculates car rental cost:

# a) Base cost is 40 per day.

# b) If days are 7 or more, apply a discount of 50.

# c) Else if days are 3 or more, apply a discount of 20.

# d) Otherwise, no discount is applied.

# e) Return the final rental cost.

# 4) Define a function `trip_cost(city, days, spending_money)` to calculate total trip cost:

# a) Add rental car cost for `days`.

# b) Add hotel cost for `days`.

# c) Add plane ride cost for `city`.

# d) Add extra `spending_money`.

# e) Return the total trip cost.

# 5) Call `rental_car_cost(5)` and print the car rental cost.

# 6) Call `plane_ride_cost("Los Angeles")` and print the plane ride cost.

# 7) Call `hotel_cost(7)` and print the hotel room cost.

# 8) Call `trip_cost("Los Angeles", 7, 500)` and print the total trip cost.

# 9) Call `trip_cost("Tampa", 6, 500)` and print the total trip cost
#  for Tampa.
def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print(rental_car_cost(5))
print(plane_ride_cost("Los Angeles"))
print(hotel_cost(7))
print(trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6, 500))