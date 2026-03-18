print("1.bike")
print("2.car")
c=int(input("Select a ride: "))
if c==1:
    print("1.Scooty")
    print("2.Scooter")
    c2=int(input("Select a ride:"))
    if c2==1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")
elif c==2:
    print("1.Sedan")
    print("2.SUV")
    c3=int(input("Select a ride:"))
    if c3==1:
        print("You have selected sedan")
    else:
        print("You have selected SUV")
else:
    print("Wrong Choice")