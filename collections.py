from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
#collections are container data types there are 4 types of collections list,set,tuple,dicitonary
#namedtuple
course = namedtuple('courses','name,platform,by')
crs = course('python','youtube','edureka')
s = course._make(['c++','edureka','pta nahi'])

print(crs)
print(s)

#deque pronounced as deck is an opmisied list to perform insertion and deletion easily
a = ['a','n','u','r','a','g']  #is a normal list
b =deque(a)     #becomes a deque
print(a)
print(b)
b.append('python')
print(b)

print(b.pop())      #removes the last value and prints it on the console
print(b.popleft())      #removes first value and prionts it on the console

#chainap is dictionary like class used to create single view of multiple mappings
a = {1:'python',2:'c++'}
b = {2: 44,5:66}

c = ChainMap(a,b)#merges two dictionaries into one
print(c)

#counter is a dicitonary subclass used to count hashable bjects
print("Counter outputs")
m = [1,2,3,4,5,6,7,8]
d = Counter(m)
print(d)
n = [1,1,1,1,2,2,2,2,23,3,3,3,3,3,4,4,4,4,4,4]
o = Counter(n)      #organises values according to maximum number of occurences
print(o)
print(list(o.elements()))   #elements() returns all the elements in the counter
print("printing most commons of counter o")
print(o.most_common())  # groups elements with their number of occurences

#ordereddict is a ordered dictionary that remembers the position in which the elements were added, even
#if the keys are changed the positions remain unchanged
ab = OrderedDict()
ab[1] = 'anurag'
ab[2] = 'nicky'
ab[3] = 'together'
print("odered dictionary")
print(ab)
print(ab.keys())

#defaultdict calls a factory function to supply missing values
mn = defaultdict(int)
mn[1] = 'a'
mn[2] = 'b'
print(mn[4])   
print(mn[41])       #supplies int 0 to both