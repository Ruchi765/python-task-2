class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available books:")
        for book in self.books:
            print(book)

    def add_book(self, new_book):
        print(f"Book '{new_book}' added.")
        self.books.insert(0, new_book)

    def borrow_book(self, book_to_borrow):
        if book_to_borrow in self.books:
            print(f"You have borrowed '{book_to_borrow}'.")
            self.books.remove(book_to_borrow)
        else:
            print(f"Sorry, the book '{book_to_borrow}' is not available.")

    def receive_book(self, returned_book):
        print(f"Book '{returned_book}' returned.")
        self.books.append(returned_book)

    def delete_book(self, book_to_delete):
        if book_to_delete in self.books:
            print(f"Book '{book_to_delete}' deleted.")
            self.books.remove(book_to_delete)
        else:
            print(f"Sorry, the book '{book_to_delete}' is not available.")

books = ['Python', 'Java', 'C', 'Ruby', 'C++']
library = Library(books)

menu = """
1. Display books
2. Add book
3. Borrow book
4. Return book
5. Delete book
6. Exit
"""

while True:
    print(menu)
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        library.list_books()
    elif choice == 2:
        book = input("Enter the book name to add: ")
        library.add_book(book)
    elif choice == 3:
        book = input("Enter the book name to borrow: ")
        library.borrow_book(book)
    elif choice == 4:
        book = input("Enter the book name to return: ")
        library.receive_book(book)
    elif choice == 5:
        book = input("Enter the book name to delete: ")
        library.delete_book(book)
    elif choice == 6:
        print("Thank you for visiting. Goodbye!")
        break
    else:
        print("You entered an invalid choice!")
