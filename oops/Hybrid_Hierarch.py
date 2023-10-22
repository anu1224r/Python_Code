#Example of Hybrid Inheritance
class baseclass:
    pass
class derivedclass1(baseclass):
    pass
class derivedclass2(baseclass):
    pass
class derivedclass3(derivedclass1,derivedclass2):
    pass

#Hierarchical-single parent-multiple child
class baseclass:
    pass
class d1(baseclass):
    pass
class d2(baseclass):
    pass
class d3(d1):
    pass