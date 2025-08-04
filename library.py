import os
class Book:
    def __init__(self,title,author,isbn,quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"     
import csv
class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def view_book(self):
        if not self.books:
            print("\nNo books in the library.")
        else:
            print("\nList of books in library: ")
            print("-" * 70)
            print("{:<20} {:<15} {:<10} {:<10}".format("Title", "Author", "ISBN", "Quantity"))
            print("-" * 70)
            for book in self.books:
                print("{:<20} {:<15} {:<10} {:<10}".format(book.title, book.author, book.isbn, book.quantity))   
                

    def search_book_by_title(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found: ")
                print(book)
                found = True
                break
        if not found:
            print("\nBook not found.")  

    def return_book(self,title):
        if not self.borrowed_books:
            print("No borrowed books to return.")
            return
        borrower = input("Enter borrower name: ").strip()
        for book in self.borrowed_books:
            if book['borrower'].lower() == borrower.lower() and book["title"].lower() == title.lower():
                self.borrowed_books.remove(book)
                for b in self.books:
                    if book['title'].lower() == title.lower():
                        book['quantity'] += 1
                        break
                self.save_borrowed_books()
                self.save_books_to_file()                
                print(f"\n'{title}' returned successfully by {borrower}.")                            
                return
        print("No matching borrowed book record found.")    

    def borrow_book(self,isbn):
        found = False
        for book in self.books:
            if str(book.isbn).strip() == isbn:
                found = True
                if book.quantity > 0:

                    borrower_name = input("Enter borrower name: ").strip()
                    from datetime import date, timedelta
                    borrow_date = date.today()
                    due_date = borrow_date + timedelta(days=7)
                    self.borrowed_books.append(
                        {
                          "isbn": book.isbn,
                          "title": book.title,
                          "borrower": borrower_name,
                          "borrow_date": borrow_date,
                          "due_date": due_date, 
                          "quantity": book.quantity
                        }
                    )          
                    book.quantity -= 1      
                    print(f"Your borrowed '{book.title}' is  borrowed successfully by {borrower_name}.")
                    return
                else:
                    print("Book is not available.") 
                    return
        if not found:            
            print("Book not found.")       

    def delete_book(self,title):
        
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Delete successfully.")
                return
        if not found:
            print("Book not found") 
                 
    def save_books_to_file(self,filename):
        try:
            with open(filename, "w") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "ISBN", "Quantity"])
                for book in self.books:
                    writer.writerow([book.title, book.author, book.isbn, book.quantity])
                    print("Books saved successfully.")
        except Exception as e:
            print("Error saving books:",e)

    def load_book_from_file(self,filename):
        try:
            with open(filename, "r")as f:
                lines = f.readlines()
                self.books = []
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) != 4:
                        print("Skipping line due to invalid format:", line)
                        continue
                    title,author,isbn,quantity = line.strip().split(",")
                    book = Book(title, author,isbn,int(quantity))
                    self.books.append(book)
                print(f"{len(self.books)} books loaded successfully.")
                self.view_book()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error loading file:",e)   

    def search_by_author(self,author):
        found = False
        for book in self.books:
            if book.author.lower() == author.lower():
                print(f"{author} books are '{book.title}'.")
                found = True
                break
        if not found:
            print("File not found.")     

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("\nNo books are currently borrowed.") 
    
        else:
            print("-" * 80)
            print("{:<15} {:<20} {:<12} {:<10} {:<10} {:<10}".format("Borrower", "Title", "Borrow date", "Due date", "ISBN", "Quantity"))
            print("-" * 80)
            
            for book in self.borrowed_books:
                borrow_date = book["borrow_date"].strftime("%d-%m-%Y")
                due_date = book["due_date"].strftime("%d-%m-%Y")
                print(f"{book['borrower']:<15} {book['title']:<20} {borrow_date:<12} {due_date:<10} {book['isbn']:<10} {book['quantity']:<10}")                                       
                print("-" * 80)
    
    def set_password(self):
        password = input("Enter password: ")
        with open("password.txt", "w") as f:
            f.write(password)
            print("Add password successfully.\n")
    def authenticate(self):
        if not os.path.exists("password.txt"):
            print("No password set.")
            self.set_password()
        with open ("password.txt", "r") as f:
            correct_password = f.read() 
            attempt = 3
            while attempt > 0:
                enter_password = input("Enter password: ")
                if enter_password == correct_password:
                    print("Authentication successfull.")
                    return True
                else:
                    attempt -= 1
                    if attempt > 0:
                        print(f"Incorrect password, Only {attempt} is left: ")
                    else:
                        print("Too many failed attempt.Exiting the program.")
                        exit()        
    def save_borrowed_books(self,filename="borrowed_books.csv"):
        with open(filename, "w", newline="")as file:
            writer = csv.writer(file)
            writer.writerow(["Borrower", "Title", "Borrow Date", "Due date", "ISBN", "Quantity"])
            for book in self.borrowed_books:
                writer.writerow([book["borrower"], book["title"], book["borrow_date"], book["due_date"], book["isbn"], book["quantity"]])            