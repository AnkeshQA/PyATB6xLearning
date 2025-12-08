import time

def print_logs(func):
    def wrapper():
        print("start of the logs")
        func()
        print("end of the logs")
    return wrapper


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper


@time_decorator
@print_logs
def test_ui_1():
    print("Running UI Test Case 1")
    time.sleep(1)  # Simulate test execution time

@time_decorator
@print_logs
def test_ui_2():
    print("Running UI Test Case 2")
    time.sleep(2)  # Simulate test execution time
test_ui_1()
test_ui_2()