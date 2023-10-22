class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The dance is {self.dance}")

class danceremployee(dancer,Employee):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
o=danceremployee("Anumeha","Kuchipudi")
print(o.name)
print(o.dance)
o.show()
print(danceremployee.mro())
