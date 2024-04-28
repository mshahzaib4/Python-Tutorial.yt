class Book:
    def __init__(self):
        self.book_id = 0
        self.price = 0
        self.page = 0

    def get(self):
        print("\t\t\t:::::::::::::::Please enter data for record::::::::::::")
        self.book_id = int(input("Enter Book ID = "))
        self.price = int(input("Enter Book price = "))
        self.page = int(input("Enter Book Page = "))

    def show(self):
        print("\t\t\t:::::::::::::::DISPLAY DATA::::::::::::")
        print("Book ID =", self.book_id)
        print("Book Price =", self.price)
        print("Book Page =", self.page)

    def set_value(self, book_id, price, page):
        self.book_id = book_id
        self.price = price
        self.page = page

def main():
    B1 = Book()
    B2 = Book()
    B3 = Book()

    B2.get()
    B3.get()

    B2.show()
    B3.show()

    B2.set_value(60, 5000, 600)
    B3.set_value(70, 3000, 200)

    print("\t\t\t::::::::::After Checking List::::::::::")
    B2.show()
    B3.show()

if __name__ == "__main__":
    main()
