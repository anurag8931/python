print("testing print functon")
name = "anurag"
#print("i am {}".format{name}) #can use any variable in place of name #not working
print(f"i am {name}")   # works smoothly

name = input("Name: ")
dynamicstring = f"i love {name}"
print(dynamicstring)