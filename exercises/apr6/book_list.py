FILE_NAME = "programs/11-file-writing/books.txt"

#write an array of books to the file books.txt
def write_books(books): #this means pass me an array of books and I will write them all to the file
    with open(FILE_NAME, "w") as file:
        for book in books:
            file.write(book + "\n")

#read in each line from the file books.txt and return an array of books
def read_books():
    books = []
    with open(FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","").strip()
            books.append(line)
    return books

#display a list of books, to the console, in formation 1. bookName
def list_books(books):
    for i in range(len(books)): # we use for i in range here instead of for book in book is bc we want to display the number associated with the book ex: book 1, book 2...
        print(f"{i+1}. {books[i]}")

#add a book to the list of books and to the file
def add_books(books):
    book = input("Book: ").strip()
    books.append(book)
    write_books(books)
    print(f"{book} was added.")
    return books

#remove a book from the list of books
def delete_book(books):
    index = int(input("Enter book number: ")) - 1

    #if the book is not in the valid range
    if index < 0 or index >= len(books):
        print(f"Sorry, valid numbers are between 1 and {len(books)}")
    else: 
        book = books.pop(index)
        write_books(books)
        print(f"{book} was deleted")
    return books

while True:
    command = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ").lower().strip()
    books = read_books()

    if command == "l":
        list_books(books)
    elif command == "a":
        books = add_books(books)
    elif command == "d":
        books = delete_book(books)
    elif command == "q":
        break
    else: 
        print("Invalid command, try again")

print("Goodbye")