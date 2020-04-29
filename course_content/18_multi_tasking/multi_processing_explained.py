from time import perf_counter
import time
from multiprocessing import Process

start_time = perf_counter()

def sample_function():
    print("Starting Function ...")
    time.sleep(3)
    print("Completed Function...")


p1 = Process(target=sample_function)
p2 = Process(target=sample_function)

p1.start()
p2.start()


# p1.join()
# p2.join()

# end_time = perf_counter()



# time.sleep(2)
# print(f"Function took {round(end_time -start_time , 2)}seconds to complete...")