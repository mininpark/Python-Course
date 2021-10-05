#FUNCTIONS IN TERMINAL 
def addSquares(x,y):
    return x**2+y**2    #don't forget to write down "return"

addSquares(3,4)

#result: 25


def fibonacci(n): #fibonacci
    fibi = [1,1]
    while len(fibi) < n:
        fibi.append(fibi[-1] + fibi[-2]) #negative number starts behind of list
    return fibi

# fibonacci (9)
# result: [1,1,2,3,5,8,13,21,34]
