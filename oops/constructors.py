class Person:
    def __init__(self,n,o):
        print("Hey I am a Person")
        self.name=n
        self.occ=o

    #name="Rahul"
    #occ="software Developer"
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("Anu","eng")

b=Person("Babu","Hero")
# print(a.name)
# a.name="Anumeha"
# a.occ="Computer Engineer"
a.info()
b.info()