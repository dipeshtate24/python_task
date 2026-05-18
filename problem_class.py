class Library:
    def __init__(self):
        self.no_books = 0
        self.books = []

    def addBooks(self, book):
        self.books.append(book)
        self.no_books = len(self.books)

    def showInfo(self):
        print(f"The current books in libray is {self.no_books}")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBooks('Harry Potter')
l1.addBooks('Life of pie')
l1.addBooks('Harry Potter2')
l1.addBooks('Harry Potter3')
l1.showInfo()
