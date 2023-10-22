class Person:
    name="Harry"
    occupation="Sofware Developer"
    networth=100

    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()
c=Person()
a.name="Babu"
a.occupation="Software Developer and DevOps"
b.name="Anu"
b.occupation="Software Engineer"
#print(a.name, a.occupation)
a.info()
b.info()
c.info()