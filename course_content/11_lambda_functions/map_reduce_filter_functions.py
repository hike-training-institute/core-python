from functools import reduce

def func():
    print("Hi World...")

def func1(x):
    # x()
    print("Welcome home...")

# func1(func)


# similarity b/w map, filter, reduce is that , they accept function as first argument
# syntax --> map(<func_name>, sequence)
# everything in python is object


def square_it(x):
    return x**2

print(tuple(map(lambda x:x**3, [1,2,3,4])))

print(list(filter(lambda x: x%2 == 0 , range(1, 100))))

print(reduce(lambda x,y: x+y, range(1, 100)))



