# Exercice : Calculatrice simple

# Créez une calculatrice simple qui prend en entrée deux nombres et un opérateur, 
# puis effectue l'opération et affiche le résultat. 
# La calculatrice doit prendre en charge les opérations suivantes : addition, soustraction, multiplication et division.

# Instructions :

# Demandez à l'utilisateur d'entrer deux nombres (float).
# Demandez à l'utilisateur d'entrer un opérateur parmi les suivants : +, -, *, /.
# Effectuez l'opération correspondante et affichez le résultat.
# Gérez les erreurs, par exemple, si l'utilisateur entre un opérateur non valide ou divise par zéro.

# Vous pouvez commencer par écrire un script qui exécute ces étapes séquentiellement.
# Une fois que vous avez terminé et testé votre script, vous pouvez améliorer votre 
# code en le transformant en une fonction 
# qui prend en entrée deux nombres et un opérateur, et qui renvoie le résultat de l'opération.

# while True : 

#     number_1 = float(input("Please enter the first number "))
#     number_2 = float(input("Please enter the second number "))
#     operator = input("Please select one opérator,  +, -, *, /. ")

#     while operator not in ["+", "-", "*", "/"]:
#         operator = input("Please select one opérator,  +, -, *, /. ")
#         print("Please enter a good operator,  +, -, *, /. ")
    
    
#     if operator == "+": 
#         solution = number_1 + number_2
#         print(solution)

#     elif operator == "-":
#         solution = number_1 - number_2
#         print(solution)

#     elif operator == "*": 
#         solution = number_1 * number_2
#         print(solution)

#     else: 
#         solution = number_1 / number_2
#         print(solution)





#     while True:
#         answer = input("Do you wish to calculate another number? [1] yes, [2] no ")
#         if answer == "2":
#             exit()
#         elif answer == "1":
#             break
#         else:
#             print("Please enter a valid value")


###### Functions type ######

# def take_number(): 
#     number1 = float(input(" Please enter your first number "))
#     number2 = float(input(" Please enter your second number "))
#     return number1, number2 

# def choice_operator(): 
#     while True: 
#         operator = input("Please select one opérator,  +, -, *, /. ")
#         if operator in ["+", "-", "*", "/"]:
#             return operator
        
#         print(" Please enter a valid operator ")
   

# def calculation(num1, num2): 
#     operator = choice_operator()
#     if operator == "+": 
#         result = num1 + num2
        
#     elif operator == "*": 
#         result = num1 * num2
    
#     elif operator == "-": 
#         result = num1 - num2

#     else : 
#         operator == "/"
#         result = num1 / num2

#     return print(result)


# def ask_recalculation(): 
#     while True:
#         new_calcul = input("Do you wish to calcul again? [1] Yes, [2], No ")
#         if new_calcul == "2" or new_calcul.lower() == "exit": 
#             print(" See you soon !")
#             return False
#         elif new_calcul == "1": 
#             return True
#         else: 
#             print(" Pleaser enter a correct digit to continue or exit ")
   
#     pass


# while True: 
#     num1, num2 = take_number()
#     calculation(num1, num2)
#     if not ask_recalculation(): 
#         break
    






# Enfin, dans votre code principal, 
# créez une instance de la classe "Calculator" et utilisez ses méthodes pour effectuer le calcul.
        

###### OOP type ######

# Créez une classe "Calculator" qui contiendra toutes les fonctions nécessaires pour effectuer le calcul.
class Calculator(): 

    def __init__(self) -> None:
        pass  

# Dans cette classe, créez une méthode "take_number" 
# qui permettra à l'utilisateur de saisir les deux nombres à calculer.
    def take_number(self): 
        num1 = float(input('Please enter a first number '))
        num2 = float(input('Please enter a seconde number '))
        return num1, num2
    
# Créez une méthode "choice_operator" qui permettra à l'utilisateur de choisir l'opérateur à utiliser.
    def choice_operator(self): 
        while True: 
                operator = input("Please enter the good operator +, -, /, *")
                if operator in ["+", "-", "*", "/"]:
                    return operator
        
                print(" Please enter a valid operator ")

# Créez une méthode "calculation" qui effectuera le calcul en fonction des deux nombres et de l'opérateur choisi.
    def calculation(self, num1, num2):
        operator = self.choice_operator()

        if operator == "+": 
            result = num1 + num2
        elif operator == "*": 
            result = num1 * num2
        elif operator == "-": 
            result = num1 - num2
        else: 
            operator == "/"
            result = num1 / num2
        return print(result)


# Créez une méthode "ask_recalculation" qui demandera à l'utilisateur s'il veut effectuer un autre calcul ou quitter le programme.

    def ask_recalculation(self): 
        while True:
            new_calcul = input("Do you wish to calcul again? [1] Yes, [2], No ")
            if new_calcul == "2" or new_calcul.lower() == "exit": 
                print(" See you soon !")
                return False
            elif new_calcul == "1": 
                return True
            else: 
                print(" Pleaser enter a correct digit to continue or exit ")
    
        pass

calculette = Calculator()
while True: 
    num1, num2 = calculette.take_number()
    result = calculette.calculation(num1, num2)
    print("Result", result)
    if not calculette.ask_recalculation():
        break 