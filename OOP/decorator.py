#decorator function must be defined before the function it is being used on/by

def time_logger(func):
    def inner_function():
        print("Function started")
        func()
        print("Function finished")
    return inner_function    


@time_logger
def greet():
    print(f"Hello ,welcome to Python decorator!")


greet()