#Assingment : 15

import gc
import tracemalloc

#start checking memory
tracemalloc.start()

#create some objects
def create_objects():
    data = []

    for i in range(1000):
        x = []
        x.append(x)
        data.append(x)

    return data

print("Starting memory check")

#create objects
data = create_objects()

#check memory before collection
current, peak = tracemalloc.get_traced_memory()
print("Memory before collection:", current, "bytes")

#delete objects
del data

#collect unused objects
collected = gc.collect()

#check memory after collection
current, peak = tracemalloc.get_traced_memory()
print("Objects collected:", collected)
print("Memory after collection:", current, "bytes")

tracemalloc.stop()

#Output
'''Starting memory check
Memory before collection: 88500 bytes
Objects collected: 1000
Memory after collection: 200 bytes'''
