class TestExecutionCounter:
    count = 0

    def __init__(self):
        TestExecutionCounter.count += 1


tex1 = TestExecutionCounter()
tex2 = TestExecutionCounter()
tex3 = TestExecutionCounter()
print(TestExecutionCounter.count)