"""
create a library class
display book
lend book
add book
return book

AjLibrary = Library(listofbooks, library_name)

you can also maintain
dictionary (books-nameofperson)

create a main function and run an infinite while loop asking users for their input
"""

class Library:
    def __init__(self, books, library_name):
        self.library_name = library_name
        self.books = books
        self.availablity_data = dict()
        self.availablity_data = dict.fromkeys(self.books, "Available")

    def add_book(self):
        """This function is to add a book to our library"""
        self.addbook = input("\nInput the name of book:")
        if self.addbook in self.books:
            print(f"{self.addbook} is already in the list")
        else:
            books = self.books.append(self.addbook)
            print(f"The book {self.addbook} added successfully")

    def display_book(self):
        """This function is to display all books in library"""
        print("Available Books are:")
        for item in self.books:
            print(f"{self.books.index(item)+1}. {item}")

    def lend_book(self):
        """This function is to lend books to user"""
        self.name = input("Please enter your name: ")
        lend_input = input("Enter the name of the book you want to lend:")
        self.lend_data =dict()
        for book in self.books:
            if book.lower() == lend_input.lower():
                self.availablity_data[book] = "Unavailable"
                if self.lend_data is None:
                    self.lend_data[book] = self.name
                else:
                    self.lend_data.update({book: self.name})
                self.books.remove(book)
                return print(f"{book} is lend to {self.name}")
            elif lend_input not in self.books:
                print("book is not in the library")
                break

    def return_book(self):
        input_book_name = input("\nPlease enter the name of book you want to return:")
        for keys, values in self.lend_data.items():
            if input_book_name.lower() == keys.lower():
                self.lend_data == self.lend_data.pop(keys)
                self.availablity_data[input_book_name] = "Available"
                books == self.books.append(input_book_name)
                return print(f"The book '{input_book_name}' returned, and added to books list successfully")

    def display_availablity(self):
        print("Availablity data is like this: ")
        for keys, values in self.availablity_data.items():
            print(keys, ':', values)

    def display_lend_data(self):
        print("Lend data is like this: ")
        for keys, values in self.lend_data.items():
            print(keys, ':', values)

if __name__ == '__main__':
    books = ['Goosebums', 'Crash Course on Python', 'Python cookbook', 'War and Peace',
             'Harry potter and the Philosophers Stone']
    mylibrary = Library(books, "AJ's Library")
    print("Welcome to Library management system")
    print("Press 'd' to display books in library\nPress 'a' to add book to library\nPress 'l' to lend a book"
          "\npress 'r' to return a book")
    print("Press 'q' to quit from the programme")
    print("\nExtra features: \nPress 'ad' to display availablity data of books\npress 'ld' to display lend data of books")
    while True:
        choice_input = input("\nInput your choice: ")
        if choice_input.lower() == "d":
            mylibrary.display_book()
        elif choice_input.lower() == "a":
            mylibrary.add_book()
        elif choice_input.lower() == "l":
            mylibrary.lend_book()
        elif choice_input.lower() == "r":
            mylibrary.return_book()
        elif choice_input.lower() == "ad":
            mylibrary.display_availablity()
        elif choice_input.lower() == "ld":
            mylibrary.display_lend_data()
        elif choice_input.lower() == "q":
            exit()
        else:
            print("Wrong Choice")
