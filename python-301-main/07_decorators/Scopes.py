def outer_func():
    msg = "Weeeeeekend!"
    def inner_func():
        print(msg)
    return inner_func

toto = outer_func()
toto()


def toto_scope():
    name = "toto"
 
    def toto_scope2():
        print(name)
        return toto_scope2
    return toto_scope2
       

toto_scope()()



# def outer_func():
#     msg = "Weeeeeekend!"
#     def inner_func():
#         print(msg)
#     return inner_func

# say_wee = outer_func()
# say_wee()  # OUTPUT: Weeeeeekend!




def decorator_func(initial_func):
    def wrapper_func():
        toto = f"{initial_func()} et je rajoute a bientot"
        return toto
    return wrapper_func # returns the wrapper func ready to be executed

def pretty():
    return "Salut les amis"

def test():
    return 'bobo'

x = decorator_func(pretty)
b = decorator_func(test)
print(x())
print(b())

# Create a decorator that repeats the output of wrapped functions twice, 
#      and use it to extend at least two different functions.

def new_decorator(ma_func): 
    def toto_wrap(): 
        calc = f' {ma_func} Salut'
        return calc
    return toto_wrap

@new_decorator
def name():
    print ('Anthony')

@new_decorator
def age(): 
    print ('37')

name()
age()

#  One possible real-world application of a basic decorator like this one would be to time the execution time of your functions. 
#  Instead of printing a message, you could print the start time before executing your initial_func(), 
#  and the end time right after it completed.

#  Write a decorator called timeit() that you can use to log 
#  the execution time of any functions you wrap with it.
import datetime


def time_decorator(my_func): 
    def wrapper_time():
        time = datetime.datetime.now()
        time_now = f'{time}'
        msg = f" {my_func()} à toi il est {time_now}"
        return msg
    return wrapper_time 

@time_decorator
def func():
    return "salut"

@time_decorator
def func2(msg):
    msg = "salut"
    return msg

print(func())




def decorator_func(initial_func):
    def wrapper_func(*args):
        print("wrapper function picked some...")
        return initial_func(*args)
    return wrapper_func

@decorator_func
def prettify(msg, msg2):
    print(msg, msg2)

@decorator_func
def feed(carbs, protein):
    print(f"{carbs} and {protein}")

prettify("flowers for you", "and chocolate")
feed("Omega3", "Chocolate")


def add_message_from(name):
    def decorator_func(initial_func):
        def wrapper_func(*args):
            print(f"{name} picked some")
            return initial_func(*args)
        return wrapper_func
    return decorator_func


@add_message_from("toto")
def prettify(msg):
    print(msg)


@add_message_from("toto")
def new_chocolate(msg):
    print(msg)

prettify("flowers for you")  # Zeek picked some flowers for you
new_chocolate("Caramel for you")


# Analogie pour expliquer le concept de "scope" en Python :

# Imaginez que vous êtes à la maison et que vous voulez dessiner un dessin.
# Vous avez une boîte de crayons de couleur sur la table devant vous.
# Vous commencez à dessiner et vous choisissez un crayon rouge pour la première partie de votre dessin.

# Le lendemain, vous revenez à la table et vous reprenez votre dessin.
# Mais cette fois, vous choisissez un crayon bleu pour la deuxième partie de votre dessin.

# Dans ce petit scénario, la table devant vous est comme un espace de travail, ou un "scope" en Python.
# Les crayons de couleur que vous utilisez sont comme les variables en Python.

# Chaque fois que vous choisissez un nouveau crayon de couleur, vous créez une nouvelle variable.
# Vous pouvez utiliser cette variable pour dessiner la partie de votre dessin que vous voulez.

# De même, lorsque vous utilisez une variable en Python, vous devez d'abord la créer dans le "scope" approprié.
# Par exemple, si vous créez une variable à l'intérieur d'une fonction, cette variable n'existe que dans le "scope" de cette fonction et n'est pas accessible à l'extérieur de celle-ci.
