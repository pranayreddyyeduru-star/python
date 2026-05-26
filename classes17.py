class computer:
    def __init__(self):
        self.maxprice=900
    def sell(self):
        print(self.maxprice)
    def setmaxprice(self,price):
        self.maxprice=price
com=computer()
com.sell()
com.setmaxprice(1200)
com.sell()
com.maxprice=1000
com.sell()