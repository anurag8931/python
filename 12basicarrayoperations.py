#arrays are mutable
""""
    operations are as follows
        1 finding length of array
        2 adding/changing elements of an array
        3 removing /deleting element(s) of an array
        4 array concatenation
        5 slicing
        6 looping through array
"""
import array 

#finding length of the array
arr = array.array('i',[1,2,3,4,5,6,7])
print(len(arr))     #len() gives the size of the array

#adding elements to an array, this can be done using append(), inset() and/or ectend()
# append() adds to the end of an array
# extend() is used to add more than one element at the end of the array
# insert() is used to insert values at a particular posiion in an array

a = array.array('i',[1,2,3,4,5])    
print("appending 6 to end of array a",a.append(6),"\n now array a  = ",a)
print("using extend()to add 7,8,9 to array a\n",a.extend([7,8,9]),"now array a = ",a)
print("using insert() to add 0 to first index of array a",a.insert(0,0),"\narray a = ",a)
print("now the length of array a = ",len(a))

#removing elements from an array using pop() or remove functin()
#pop() is used when we want to remove an element and return it - when not specified pops lasst element, takes index value as argument
#remove() is used when we want to remove a specific value without returning it takes value as an arg
#remove removes first occurence of value

print("removing last indexed element from a. the element is = ",a.pop())
print("array is ",a)
print("removing 5th indexed value from a. the element is = ",a.pop(5))
print("array is ",a)
print("removing last indexed element from a using arg -1. the element is = ",a.pop(-1))
print("array is ",a)
print("removing value 4 from array",a.remove(4))
print("array is ",a)

#array concatenation done using + operator
b = array.array('i',[1,2,3,4,5])
c = array.array('i',[6,7,8,9,10])
d = b+c
print(d)

#slicing an array means fetching some particular values from the array
print("sliced array d from 0 to 4(excluded) is  ",d[0:4])   #returns indexes 0,1,2,3
print("sliced array d from 0 to -2(excluded,second last element) is  ",d[0:-2])   
print(d)

print(d[::-1])  #prints a reversed COPY of the array with index = index-1 
#mtlb agr -3 use kia to 10 7 4 1 aise index k values hi print honge
#not preferred as is memory exhaustive

#looping using for/while

print("printing all values in b using a for loop")
for x in b:
    print(x)
print("")
for x in d[0:-7]:
    print(x)

print("printing using while loop")
temp = 0 #iterator for the loop
while temp<d[5]:
    print(d[temp])
    temp = temp+1

print("using len for while")
tem = 0
while tem<len(d):
    print(d[tem])
    tem+= 1