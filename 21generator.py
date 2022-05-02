#are functions that return traversable objects
#produce items one at a tim and only when required
#run along with for loops

#use yield rather than return
#called by next() rather than function name
#produce one item at a time unlike functions that produce all items at once

def new(dict):
    for x,y in dict.items():
        yield x,y

a = { 1:"hii",2:"Welcome" }
b = new(a)
print(b)
next(b)