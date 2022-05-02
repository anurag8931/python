#lambda functions are known as throwaway funcitons or anonymous fuctions
#used as arguments for grts functions
#lambda functions can take nay number of arguments
x = lambda  a: a*a

print(x(3))

#lambda within user defined function
def sum(z):
    return (lambda y:z+y)

t = sum(4)
print(t(2))

#using lambda function within filter() map() and reduce() functions

list1 = [1,2,3,4,5]
newlist = list(filter(lambda a:(a%2==0),list1)) #filter(function,iterable)
print(newlist)

#map() applies funciton to all elements and returns a new list
p = list(map(lambda a:(a%2!=0),list1))
print(p)

#reduce() returns a single value after applying a function to all elements
#reduce(function,sequence)
from functools import reduce # can also use import functools or from functools import *
print(reduce(lambda a,b:a+b,list1))

#more sue of lambda function
print("more use of lambda function")
asqb = lambda a,b: a*a+b*b+2*a*b
print(asqb(4,2))
