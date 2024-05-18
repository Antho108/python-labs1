# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.

# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class DoctorForm():
    """Creater an empty Doctor form
    """
    def __init__(self, name, phone, adress, city) -> None:
        self.name = name 
        self.phone = phone 
        self.adress = adress
        self.city = city
    
    def say_hello(self): 
        print ("Welcome to the doctor ", self.name)

    def MedicalExam(self, health, weight, medicalissue):
      
        self.health = health 
        self.patern = weight 
        self.medicalissue = medicalissue
       

    def __str__(self):
        return f"{self.name} ({self.city}) ({self.health}) ({self.medicalissue})"




toto = DoctorForm("Jean", 43433, "23 street bellevue", "NYC")
toto.say_hello()
toto.MedicalExam("Ok", 98, 'Cold')
print(toto)
