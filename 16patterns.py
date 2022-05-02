#star patterns
#pyramid 1
#this is a function definition
def pattern(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k-=1
        for j in range (0,i+1):
            print("*",end=" ")
        print('\r')

pattern(5)

# 3:40 to 4:24 for patterns