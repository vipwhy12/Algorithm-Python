

def fib(n):
    if n < 3:
        return 1
    return fib(n)
    
for i in range(1, 11):
    print(fib(i))
    