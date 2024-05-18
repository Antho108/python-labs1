def say_hi():
    print("Hi.")


say_hi()

hi = say_hi
hi()


def say_moo():
    print("moooooooo!")

list_ = [say_hi, say_moo]
print(list_[0](), list_[1]())
print(list_)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __call__(self):
        print("This is a", self.make, self.model)

my_car = Car("Toyota", "Corolla")
my_car()  # Output: This is a Toyota Corolla



# La méthode __call__() en Python permet de faire en sorte qu'un objet puisse être appelé 
# comme une fonction. Cela signifie que vous pouvez créer des objets qui se comportent comme des fonctions.

# Par exemple, si vous créez un objet my_object qui a une méthode __call__(),
#  vous pouvez appeler cet objet comme s'il s'agissait d'une fonction en écrivant my_object().

# La méthode __call__() peut prendre des arguments, tout comme une fonction normale, 
# et peut retourner une valeur.
