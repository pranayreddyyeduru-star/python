class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return (f"{self.x, self.y}")
pon=point(2,3)
print(pon)