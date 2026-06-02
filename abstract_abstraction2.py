class India():
    def capital(self):
        print("New Delhi is the Capital of India")
    def language(self):
        print("Hindi is the most spoken language in India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA")
    def language(self):
        print("English is the primary language in the US")
    def type(self):
        print("USA is a developed country")
obj_ind=India()
obj_usa=USA()
for i in (obj_ind,obj_usa):
    i.capital()
    i.language()
    i.type()