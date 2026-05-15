class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX=Vehicle(240, 18)
print("Model X has a maximum speed of",modelX.max_speed,"km/h and mileage of",modelX.mileage,"km/l")