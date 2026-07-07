from library import Library
from book import Book
from member import Member

library = Library()
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Add Member")
    print("6. Display Members")
    print("7. Search Member")
    print("8. Remove Member")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        isbn = input("Enter ISBN: ")
        genre = input("Enter Genre: ")
        book = Book(title, author, isbn, genre)
        library.add_book(book)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        isbn = input("Enter ISBN to search: ")
        library.search_book(isbn)

    elif choice == "4":
        isbn = input("Enter ISBN to remove: ")
        library.remove_book(isbn)

    elif choice == "5":
        name = input("Enter Member Name: ")
        member_id = input("Enter Member ID: ")
        contact = input("Enter Contact Number: ")
        member = Member(name, member_id, contact)
        library.add_member(member)

    elif choice == "6":
        library.display_members()

    elif choice == "7":
        member_id = input("Enter Member ID to search: ")
        library.search_member(member_id)

    elif choice == "8":
        member_id = input("Enter Member ID to remove: ")
        library.remove_member(member_id)

    elif choice == "9":
        isbn = input("Enter Book ISBN: ")
        member_id = input("Enter Member ID: ")
        library.borrow_book(isbn, member_id)

    elif choice == "10":
        isbn = input("Enter Book ISBN: ")
        member_id = input("Enter Member ID: ")
        library.return_book(isbn, member_id)

    elif choice == "0":
        print("Thank you for using the Library Management System!")
        break
    
    else:
        print("Invalid choice! Please try again.")
