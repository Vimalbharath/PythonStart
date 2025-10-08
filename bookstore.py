# ---- Book Class ----
class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - ${self.price}"

# ---- User Class ----
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# ---- CartItem Class ----
class CartItem:
    def __init__(self, book, qty):
        self.book = book
        self.qty = qty

    def total_price(self):
        return self.book.price * self.qty

# ---- ShoppingCart Class ----
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_book(self, book, qty):
        self.items.append(CartItem(book, qty))

    def calculate_total(self):
        return sum(i.total_price() for i in self.items)

# ---- Order Class ----
class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.total_amount = sum(i.total_price() for i in items)
        self.status = "Pending"

    def set_status(self, status):
        self.status = status

# ---- Payment Class ----
class Payment:
    def process_payment(self, user, amount):
        print(f"Processing payment of ${amount} for {user.name}")
        return True

# ---- BookStore Class ----
class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for b in self.books:
            print(b)

    def search_by_title(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

# ---- Main ----
if __name__ == "__main__":
    store = BookStore()
    store.add_book(Book("Clean Code", "Robert C. Martin", "111", 40.0))
    store.add_book(Book("Design Patterns", "GoF", "222", 50.0))

    user = User("Alice", "alice@email.com")

    store.display_books()
    cart = ShoppingCart()
    book1 = store.search_by_title("Clean Code")
    if book1:
        cart.add_book(book1, 2)

    order = Order(user, cart.items)
    payment = Payment()
    if payment.process_payment(user, order.total_amount):
        order.set_status("Paid")

    print("Order Status:", order.status)