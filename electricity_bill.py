u=int(input("Enter the number of electricty units consumed:"))
if u<50:
    a=u*2.60
    s=25
elif u<=100:
    a=130+((u-50)*3.25)
    s=35
elif u<=200:
    a=292.5+((u-100)*5.26)
    s=45
else:
    818.5+((u-200)*8.45)
    s=75
total=a+s
print(total)
