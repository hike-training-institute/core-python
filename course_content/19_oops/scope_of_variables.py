x = 10 # global variable

def func():
    x = 20  # local variable
    print(x)


class Sample:
    x = 30 # class variable - accessed using class Name or the instance

    def func_inside_a_class(self):
        x = 40 # local variable
        print(self.x) # instance variable
        print(x)
        print(Sample.x)
        self.x = 555

ram = Sample()
ram.x = 444
ram.func_inside_a_class()

ravi = Sample()
ravi.func_inside_a_class()

print(Sample.__dict__)
print(ram.__dict__)
print(ravi.__dict__)
