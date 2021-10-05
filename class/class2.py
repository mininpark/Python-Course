#FUNCTIONS IN TERMINAL 
#>>> def addSquares(x,y)
#...    return x**2+y**2
#...    
#addSquares(3,4)

#result: 25


def fib(n):
    fibi = [1,1]
    while len(fibi) < n:
        fibi.append(fibi[-1] + fibi[-2])
    return fibi
    