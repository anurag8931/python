x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

fruits = ("apple", "banana", "cherry")  #packing a tuple
(green, yellow, red) = fruits       #unpacking a tuple

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits      #* assigns an arrya for excess values of the tuple

print(green)
print(tropic)
print(red)
