#while is used when we are not sure of number of iterations required
count = 0
while count<9:
    print("count = ",count)
    count+=1

#guessing game using while
#while is used as not sure when someone will guess correct number
import random
# un comment to see this example
"""
n = 20
guess = int(n*random.random())
gues = 0
while gues != guess:
    gues = int(input("Guess a number : "))
    if gues > 0:
        if gues > guess:
            print("Number is too large")
        elif gues < guess:
            print("Number is too small")
    else:
        print("sorry, wrong guess")
else:
    print("Congratulations, you won")
"""
#for loops are used when we know the number of times iterations are needed to run
"""
    for variable in range:
"""
avengers = ['iron man','captain america','spider man','natasha','hulk','thor','hawkeye']

for i in avengers:
    print(i)

#factorial
num = int(input("enter a number to calculate factorial : "))
factorial = 1;
if num < 0:
    print("To calculate factorial number must be positive")
elif num==0:
    factorial = 1;
else:
    for i in range(1,num+1):
        factorial*=i;

print("factorial is ",factorial)