from timing_decorator import measure_execution_time

@measure_execution_time
def testHelloWorld():
    print('Say hello world!')

@measure_execution_time
def testShortLoop():
    print('\nShort loop')
    for i in range(11000000):
        pass
    pass

@measure_execution_time
def testNotSoShortLoop():
    print('\nNot so short loop')
    for i in range(300000000):
        pass
    pass

testHelloWorld()
testShortLoop()
testNotSoShortLoop()