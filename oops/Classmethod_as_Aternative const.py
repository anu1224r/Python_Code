class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  @classmethod
  def fromStr(cls,string):
    return cls(string.split("-")[0], string.split("-")[1])
e=Employee("Anu",12000)
print("the salary is in $ not rs")
print(e.name)
print(e.salary)

string="Anum-9000"
#e2=Employee(string.split("-")[0], string.split("-")[1])
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)