from datetime import datetime as dt

def time_it(x):

    def actual_decorator_implementation():
        t1 = dt.now()
        print("welcome for decoration", t1)

        x()

        t2 = dt.now()
        print("Thanks for choosing us , decoration is done", t2)
        print("Time taken : ", t2 - t1)


    return actual_decorator_implementation

@time_it
def func1():
    import time
    time.sleep(3)
    print("Hi , am here for decoration pls decorate me...")

@time_it
def func2():
    pass

func1()
func2()