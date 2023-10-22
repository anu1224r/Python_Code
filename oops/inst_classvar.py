class Employee:
    CompanyName="Apple"
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
    def showDetails(self):
        print(f"the name of the Employee is {self.name} and raise amount in {self.CompanyName} is {self.raise_amount}")

emp1=Employee("Anu")
emp1.raise_amount=0.3
emp1.CompanyName="Apple India"
emp1.showDetails()
emp2=Employee("babu")
emp2.showDetails()
#Employee.showDetails(emp1)