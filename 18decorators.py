#in python everything is an object, even a fcuntion. a function can be passed as an argument
#and hence is called first-class object
#inner function is a function declared inside a function

def fun1(name):
    return f"Hello {name}"

def fun2(name):
    return f"{name} ,How you doin?"

def fun3(fun4):
    return fun4('Hey learner')

print(fun3(fun1))
print(fun3(fun2))

#inner functions
print("\n inner functions below\n")
def func():
    print('parent function')
    def func1():
        print("inner function 1")
    def func2():
        print("inner function 2")
    
    func2()
    func1()

func()

#returning a function

def function1(n):
    def funct1():
        return "its 1"
    def funct2():
        print("its 2")
    if n==1:
        return funct1
    else:
        return funct2
    
a = function1(1)
b = function1(2)

print(a())
print(b())