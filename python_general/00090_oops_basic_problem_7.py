# Create a `Book` class with attributes `title`, `author`, and `price`. Add a method `discounted_price(discount)` which returns price after reducing the discount percentage.

class Book :
    title = 'book title'
    author = 'author'
    price = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def discounted_price(self, discount) :
        print(f"Discounted price is {self.price - self.price * (discount / 100)}")

book1 = Book('Probability and Statistics', 'Arnab Chakraborty', 250)

book1.discounted_price(5)