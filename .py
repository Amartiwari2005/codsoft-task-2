# Define an empty dictionary to store book data
books = {}

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    books[title] = author
    print(f"{title} by {author} has been added to the library.")

def view_books():
    if not books:
        print("The library is empty.")
    else:
        print("Library Contents:")
        for title, author in books.items():
            print(f"{title} by {author}")

def save_books_to_file():
    with open("books.txt", "w") as file:
        for title, author in books.items():
            file.write(f"{title},{author}\n")
    print("Library data saved to 'books.txt'")

def load_books_from_file():
    try:
        with open("books.txt", "r") as file:
            for line in file:
                title, author = line.strip().split(',')
                books[title] = author
        print("Library data loaded from 'books.txt'")
    except FileNotFoundError:
        print("No library data found. Create a library first.")

while True:
    print("\nBook Content Program")
    print("1. Add a book")
    print("2. View books")
    print("3. Save to file")
    print("4. Load from file")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        save_books_to_file()
    elif choice == "4":
        load_books_from_file()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")


This program allows you to add books, view the library's contents, save the data to a file, and load data from a file. You can run this program in a Python environment, and it will interactively manage your book content.

Here's how it works:

1. You run the program, and a menu is displayed.
2. You can choose options like adding books, viewing the library, saving the data, or loading data from a file.
3. The data is stored in a dictionary with book titles as keys and authors as values.
4. When you save to a file, the data is written to a text file.
5. When you load from a file, it reads the data from the file (if available) and populates the library.
6. You can exit the program by selecting option 5.

Remember to create a "books.txt" file in the same directory as the script before you use the "Save to file" or "Load from file" options.