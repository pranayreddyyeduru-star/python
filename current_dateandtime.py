from datetime import date, time, datetime
today=date.today()
now=datetime.now()
print("Today's date is", today)
print("\n The current date and time is ", now)
print("\nDate components", today.month, today.day, today.year)