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

    def display_members(self):
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

    def borrow_book(self,isbn,member_id):
        book_found=None
        member_found=None
        for book in self.books:
            if isbn==book.isbn:
                book_found=book 
                break
        if book_found is None:
            print("Book Not Found")
            return   

        for member in self.members:
            if member_id==member.member_id:
                member_found=member
                break
        if member_found is None:
            print("Member Not Found")
            return
         
        if not book_found.available:
            print("Book is already borrowed")
            return
        book_found.availability= False
        book_found.borrowed_by=member_id
        member_found.books_borrowed.append(book_found.isbn)
        print("Book borrowed successfully")

    def return_book(self,isbn,member_id):
        book_found=None
        member_found=None
        for book in self.books:
            if isbn==book.isbn:
                book_found=book 
                break
        if book_found is None:
            print("Book Not Found")
            return  

        for member in self.members:
            if member_id==member.member_id:
                member_found=member
                break
        if member_found is None:
            print("Member Not Found")
            return
        if book_found.available:
            print("Book is already availabe")
            return
        if book_found.borrowed_by != member_id:
            print("This member did not borrow this book.")
            return

        book_found.available = True
        book_found.borrowed_by = None
        member_found.books_borrowed.remove(book_found.isbn)
        print("Book returned successfully!")


        
