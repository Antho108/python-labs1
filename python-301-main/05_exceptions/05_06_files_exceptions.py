# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


from pathlib import Path

book1_path = Path("python-301-main/05_exceptions/books/war_and_peace.txt")
book2_path = Path("python-301-main/05_exceptions/books/crime_and_punishment.txt")
book3_path = Path("python-301-main/05_exceptions/books/pride_and_prejudice.txt")

# Task 1: Read the whole content of war_and_peace.txt
with book1_path.open("r") as book1_file:
    content_1 = book1_file.read()
    print(f"First letter of first text is {content_1[0]}")

# Task 2: Overwrite the whole content of crime_and_punishment.txt with an empty string
with book2_path.open("w") as book2_file:
    book2_file.write("")

# Task 3: Loop over all three files and print out only the first character each, without terminating with a traceback
book_paths = [book1_path, book2_path, book3_path]
for path in book_paths:
    try:
        with path.open("r") as book_file:
            first_character = book_file.read(1)
            print(f"First letter of {path}: {first_character}")
    except Exception as e:
        print(f"An error occurred while reading {path}: {str(e)}")



    
