class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blue=Parrot("Blue",10)
woo=Parrot("Woo",15)
print("Blue is a",blue.__class__.species)
print("Woo is a",woo.__class__.species)
print("Blue is",blue.age,"years old")
print("Woo is",woo.age,"years old")
