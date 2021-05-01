import array
import weakref

import class_decorator

my_array1 = array.array('i', [1,2,3,5,6,9])
my_array2 = array.array('u', "some random string")
my_array3 = array.array('i', [True, False])
my_array4 = array.array('L',)

class Thing():
    pass

for _ in range(10):
    my_thing = Thing()
    weak_ref = weakref.ref(my_thing)
    my_array4.append(weak_ref())

for item in locals():
    try:
        print(f"{item}")
    except Exception as e:
        print(f"{e}")
        pass