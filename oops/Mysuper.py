class ParentClass:
    def parent_method(self):
        print("this is the parent method")
class ChildClass(ParentClass):
    def parent_method(self):
        print("anu")
        super().parent_method()
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object=ChildClass()
child_object.child_method()