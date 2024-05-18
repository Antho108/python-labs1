# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?


class Movie() : 

    def __init__(self, year, title, director):
        self.year = year 
        self.title = title 
        self.director = director 
    pass

    def release(self): 
        if self.year > 2022 : 
            print(f'This movie, {self.title} will come soon')

        elif self.year < 2022:
            print(f' {self.title} can be watch in streaming! ') 
        
        else:
            print(f'{self.title} is actually at the cinema! ')

    def type(self): 
        print(f'This movie is for everyone')
        pass

    def __str__(self) -> str:
        return f'This movie is {self.title}, created in {self.year} and realised by {self.director}'

class RomCom(Movie):

    def type(self): 
        print(f'This movie is for people who loves comedy')
         
    pass

class ActionMovie(Movie): 
    
    def __init__(self, year, title, director, pg):
        super().__init__(year, title, director)
        self.pg = 13

    
    def type(self): 
        print(f'This movie is for people who loves Action')



avatar = Movie(2010, "Avatar", "James")
print(avatar)
avatar.release()

b = ActionMovie(200, "Golden eyes", "Roro", 13)
b.type()

r = RomCom(1990, "Les bronzes font du ski", "Lelouche")
r.type()
print(b)
print(r)
r.release()
b.release()