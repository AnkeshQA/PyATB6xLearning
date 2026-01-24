count = 0

def increment():
    global count # this is global variable . we have to give keyword using global
    count += 1

increment()
print(count)