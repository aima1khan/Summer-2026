class Member:
    def __init__(self,name,member_id,contact_no):
        self.name=name
        self.member_id=member_id
        self.contact_no=contact_no
        self.books_borrowed=[]

    def display(self):
        print("====Member Information==== ")
        print(f"Name : {self.name}")
        print(f"ID : {self.member_id}")
        print(f"Contact : {self.contact_no}")
        if self.books_borrowed:
            print("Books Borrowed :")
            for book in self.books_borrowed:
                print(book.display())
        else:
            print("No Books Borrowed yet!")