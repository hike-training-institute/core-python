def sample_function():
    print("sample function is called...")

class Hand():
    finger = 5

    def hand_func(self):
        print("Hi I am from Hand class")

class Leg():
    toe_color = 'white'

class Human(Hand, Leg): # inheritence
    eyes = 2
    finger = 10 # overriding

    def __init__(self, name, age=27):  # constructors
        print("am not called anywhere... but i get executed automatically")

    def func(self, x, y, z):
        print("Hi World...")

    def hand_func(self):
        print("Hi I am from Human Class")

    def print_inherited_props(self):
        print(self.finger)  # finger inherited from Hand class

    def __del__(self): # destructor
        print("am not called anywhere ... but i get executed when you delete instance")

    @staticmethod
    def sample_static_method():
        print("sample static method is called...")

    @classmethod
    def sample_class_method(cls):
        print("sample class method is called...", cls.finger)

class Employee(Human):

    def __init__(self):
        pass

ram = Employee()
ram.hand_func()

ram.sample_static_method()
Human.sample_static_method()

ram.sample_class_method()
Human.sample_class_method()