def fib(n):
    if (n <= 2):
        return 1
    else:
        f = fib(n - 1) + fib(n - 2)
        return f
    
print(fib(10))


def fibo(n):
    for k in range(n):
        if n <= 2:
            f = 1
            return f
        else:
            f = fib(n-1) + fib(n-2)	
            return f


print(fibo(10))