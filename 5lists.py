# lists are like arrays initialised using []

fruits = ['apple','kiwi','grapes']

print(type(fruits))
print(fruits)

list2 = [1,3,'qwerty',4.556]    #a list can aslo hold different values
print(type(list2))
print(list2)

#accessing list values using index numbers
print(fruits[2])
print(list2[2])

#funcitons for list
list2.append("appendedvalue")
list2.insert(4,'insertedvalue')
list2.reverse()
print(list2)