class AgeError(Exception):
    def __init__(self, age):
        self.age = age


age = int(input("Age: "))

if age < 0:
    # raise AgeError(age)
    raise Exception(42)