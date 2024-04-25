def fibonacci(limit):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > limit:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

limit = int(input("Enter the limit for Fibonacci numbers generation: "))
fib_numbers = fibonacci(limit)
print("Fibonacci numbers up to", limit, "are:", fib_numbers)
