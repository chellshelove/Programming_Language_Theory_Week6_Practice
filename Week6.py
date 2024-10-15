import time

# Regular Recursive Fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Tail Recursive Fibonacci with a helper function
def fib_tr_helper(n, pp, p):
    if n == 1:
        return pp
    if n == 2:
        return p
    return fib_tr_helper(n - 1, p, pp + p)

# Wrapper for convenience
def fib_tr(n):
    return fib_tr_helper(n, 1, 1)

# Measure execution time for recursive Fibonacci
start_time = time.time()
fib_result = fib(40)  # You can change this to 50 if the execution is fast enough
end_time = time.time()
print(f"Recursive Fibonacci result: {fib_result}")
print(f"Recursive Fibonacci execution time: {end_time - start_time:.6f} seconds")

# Measure execution time for tail recursive Fibonacci
start_time = time.time()
fib_tr_result = fib_tr(40)  # You can change this to 50 if the execution is fast enough
end_time = time.time()
print(f"Tail Recursive Fibonacci result: {fib_tr_result}")
print(f"Tail Recursive Fibonacci execution time: {end_time - start_time:.6f} seconds")

# Example of a sum function in tail-recursive form
def sum_tr_helper(n, acc):
    if n == 0:
        return acc
    return sum_tr_helper(n - 1, acc + n)

def sum_tr(n):
    return sum_tr_helper(n, 0)

# Measure execution time for tail recursive sum
start_time = time.time()
sum_tr_result = sum_tr(100)
end_time = time.time()
print(f"Tail Recursive Sum result: {sum_tr_result}")
print(f"Tail Recursive Sum execution time: {end_time - start_time:.6f} seconds")