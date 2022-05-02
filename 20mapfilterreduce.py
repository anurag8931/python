#map() applies a given function to all iterables and returns a new list
#filter() consists an output of values which function evaluates as true
#reduce() applies function to iterables and returns a single value


#map(function,iterables)
#map with user defined functions

def new(a):
    return a*a

x = list(map(new,[1,2,3,4,5]))  # can convert to list tuple etc anything map can take more than 2 parameters
print(x)    #returns a list with sq of every element of the list

#filter()
print("filter function with user defined function")
def new1(i):
    if i>=2:
        return i

j = tuple(filter(new1,(1,2,3,4,5)))
print(j)    #prints elements only greater than 2 from the tuple

#reduce()
print("reduce function with user defined function")
from functools import *
def new2(x,y):
    return x+y
s = reduce(new2,[1,2,3,4,5,5])
print(s)

#filter within map
print("using filter within map")

c = list(map(lambda a:a*2,filter(lambda a:a>=5,[5,1,2,55,60])))
print(c)

#map within filter
print("similarly using map wihtin filter")
d = list(filter(lambda a:a>=100,map(lambda a:a*10,[10,2,20,15,14])))
print(d)

#using map and filter within reduce
print("using map and filter within reduce")
r = reduce(lambda x,y:x+y,map(lambda x:x+10,filter(lambda x:x<=5,[1,2,3,4,5,6,7,8,9])))
print(r)