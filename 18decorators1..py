def fun(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to learning decorators")
    return wrapper

def func():
        print("new function")

func = fun(func)

func()

"""
def fun(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to learning decorators")
    return wrapper

@fun
def func():
    print("newfunciton")

func()
"""