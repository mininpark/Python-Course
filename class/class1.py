fib = [1,1]

for i in range(1,9):
    fib.append(fib[-1] + fib[-2])

fib = [1,1]
while len(fib) < 10:fib.append(fib[-1] + fib[-2])

