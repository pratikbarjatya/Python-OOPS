class Father:
    def father_property(self):
        print('Father property used for home')


class Mother(Father):
    def mother_property(self):
        print('Mother property used for farming')


class Child(Mother):
    def child_property(self):
        print('child property used for playground')

    def father_property(self):
        print('Father property now used by child for cricket ground.')


obj1 = Child()
obj1.father_property()
obj1.mother_property()
obj1.child_property()
