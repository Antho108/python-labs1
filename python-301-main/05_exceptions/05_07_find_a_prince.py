# Write a custom exception  that inherits from `Exception()`

# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


from pathlib import Path

class PrincException(Exception): 

    def __init__(self, word):
        self.word = word


    def findtheword(self, contenu):
        if self.word in contenu[:100]: 
            raise PrincException(" We found the small prince ")
        else: 
            raise PrincException( " We lost the small prince ")


books = Path("python-301-main/05_exceptions/books")

for fichier in books.glob("*.txt"):
    with fichier.open("r") as f:
        contenu = f.read()
        
    try:
        p = PrincException("Prince")
        p.findtheword(contenu)
    except PrincException as e:
        print(e)



   





