x=[1,2,3]
dir(dir(x))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
p=Person("Anu",25)
print(p.__dict__)
#print(help(Person))