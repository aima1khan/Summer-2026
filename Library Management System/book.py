class Book:
    def __init__(self,title,author,isbn,genre):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.genre=genre
        self.available=True
        self.borrowed_by=None

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN : {self.isbn}")
        print(f"Genre : {self.genre}")
        if self.available:
            print("Availability : Available")
        else:
            print("Availability : Not Available")
            print(f"Borrowed by : {self.borrowed_by}")
        