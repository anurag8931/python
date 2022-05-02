import pandas as pd
#hash table or hashmap is a data structure that maps keys to its  value pairs
#dictionary in python can be created using either {} or dict()

#{} method
dict1 = {'name':'anurag','partner':'nicky'}

dict2 = dict(anurag='001',nicky='002')
print(dict2)
print(type(dict2))

#nested dictionaries
"""
consider a team of employes as a dictionary, now each employee will hav info so thats nested dictionary
"""
dict3 = {'employee':{'anurag':{'id':'1','desig':'jobless'},'nicky':{'id':'2','desig':'earning'}}}
print(dict3)

#accessing value using key value
print("accessing value using key value")
print(dict1['name'])
print(dict1)
print("getting all the keys")
print(dict1.keys())
print("getting all the values")
print(dict1.values())
print("using get to get value of a particular key")
print(dict1.get('partner'))

print("using for to get all the keys only")
for x in dict1:
    print(x)

print("using for to get all the values only")
for x in dict1.values():
    print(x) 

print("using for to get all the key-value pairs")
for x in dict1.items(): #print  like (key,value) with ach set in new line
    print(x)

print("using for to get all the key-value pairs")
for x,y in dict1.items():   #print  like key value with ach set in new line
    print(x,y)

#updating values of dictionary as they are mutable data types
dict1['name'] = "toppr" #changing value of the key name
print(dict1)

#ading new key value
dict1['relation'] = 'lovers'    #adding new key value pair
print(dict1)

#deleting values from dictionary
#pop() it takes key as argument and pops the value for mentioned key
print(dict1.pop('relation'))    #popped/removed key value pair for key relation
print(dict1)

#popitem() pops last added item to dictionary
dict1['relation'] = 'lovers'
print("popped last item in the dictionary   ",dict1.popitem())
print(dict1)

#using del
print("deletion using del")
dict1['relation'] = 'lovers'
del dict1['relation']
print(dict1)

#converting a dictionary into a dataframe
#DATAFRAME IS A 2d data structure that consists columns of various types. being similar to python dictionary it 
#can easibly be converted to pandas dataframe
#dictionary to data frame

#allows to use pd in place of pandas remember array as ar?
print("converting dictionary to data frame\n\n")
df = pd.DataFrame(dict3['employee'])
print(df)
