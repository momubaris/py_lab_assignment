class Book:
  def __init__(self, title, author, price):
    self.title = title
    self.author = author
    self.price = price
  def display(self):
    print("Title:", self.title)
    print("Author:", self.author)
    print("Price:", self.price)
  def apply_discount(self, discount):
    self.price = self.price - (self.price * discount)
class EBook(Book):
  def __init__(self, title, author, price, format):
    super().__init__(title, author, price)
    self.format = format
  def display(self):
    print("Title:", self.title)
    print("Author:", self.author)
    print("Price:", self.price)
    print("Format:", self.format)
def main():
  book = Book("The Da Vinci Code","Dan Brown",24.99)
  book.display()
  book.apply_discount(0.10)
  print("New price:",book.price)
  ebook = EBook("The Hunger Games", "Suzanne Collins", 19.99, "Kindle")
  ebook.display()
if __name__ == "__main__":
  main()
