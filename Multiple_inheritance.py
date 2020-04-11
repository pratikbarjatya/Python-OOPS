class Father:
    def father_property(self):
        print('Father Property')


class Mother:
    def mother_property(self):
        print('Mother Property')


class Child(Father, Mother):
    def child_property(self):
        print('Child will inherit using Super : ')
        super().father_property()
        super().mother_property()


obj1 = Child()
obj1.child_property()
print('Calling Mother And Father by instance of the child Class:')
obj1.mother_property()
obj1.father_property()
