class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee:{self.id} is {self.name}")
class Programmer(Employee):
    def showLanguage(self):
        print("the default language is python")
e1=Employee("Babu lal",423)
e2=Programmer("anumeha",2424)
e1.showDetails()
e2.showDetails()
e2.showLanguage()