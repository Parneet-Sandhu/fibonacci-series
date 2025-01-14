def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"First {n} numbers of Fibonacci series: {result}")