# What are Static (Class) Variables?
# Static (also called **class**) variables are **shared by all objects** of a class.
#  They belong to the **class itself**, not to any particular object instance.

class TestCounter:
    count = 0

    def __init__(self):
        TestCounter.count +=1



t1 = TestCounter()
t2 = TestCounter()
print(TestCounter.count)

#Each time an object is created, count increases.
# count is shared across all objects.