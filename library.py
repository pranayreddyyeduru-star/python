class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        is_borrowed=False
        print("It isn't borrowed")
    def borrow(self):
        is_borrowed=True
        print("It is borrowed")
    def return_book(self):
        is_borrowed=False
        print("The book is returned")
book=Book("Percy Jackson", "Rick Riordan")
book.borrow()
book.return_book()
book.self()