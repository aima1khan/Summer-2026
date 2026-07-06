class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    
    def add_book(self,book):
        self.books.append(book)
        print("Book Added Successfully!")

    def display_books(self):
        if self.books:
            print("=====Displaying Books=====")
            for book in self.books:
                book.display()
        else:
            print("No Books Found")

    def add_member(self,member):
        self.members.append(member)
        print("Member Added Successfully!")

    def display_member(self):
        if not self.members:
            print("No Member Found")
        else:
            for member in self.members:
                member.display()

    def search_book(self,isbn):
        for book in self.books:
            if isbn==book.isbn:
                book.display()
                return            
        print("No Match Found!")

    def remove_book(self,isbn):
        for book in self.books:
            if isbn==book.isbn:
                self.books.remove(book)
                print("Book Removed Successfully!")
                return
        print("No Book Found!")

    def search_member(self,member_id):
        for member in self.members:
            if member_id==member.member_id:
                member.display()
                return
        print("No Match Found")

    def remove_member(self,member_id):
        for member in self.members:
            if member_id==member.member_id:
                self.members.remove(member)                
                return
        print("No Match Found")



        
