# Écrivez une fonction qui prend un paramètre numérique et calcule sa racine carrée.
# Gérez l'erreur si le nombre est négatif et renvoyez une exception appropriée.
# Testez votre fonction en appelant la fonction avec des valeurs positives et négatives et 
# vérifiez que les exceptions sont levées lorsque c'est nécessaire.

import math

class NegativeNumberError(Exception):
    
    pass

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Le nombre ne peut pas être négatif")
    return math.sqrt(number)

try:
    print(calculate_square_root(11))  # doit afficher 3.0
    print(calculate_square_root(-1))  # doit lever une exception
except NegativeNumberError as e:
    print(e)
