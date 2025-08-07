class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    #start with other
    #do not say self.other again
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

book1 = Book("DOAC", "Steven", 279)
book2 = Book("Think and Grow Rich", "Napoleon", 300)

print(book1)

print(book1 == book2)

print(book1 > book2)
print(book1 < book2)

print(book1 + book2)

print("Steven" in book1)