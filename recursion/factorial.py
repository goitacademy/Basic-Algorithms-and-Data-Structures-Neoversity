# Iterative
def factorial_iterative_while(n):  # Condition-controlled version
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

# Recursive
def factorial_recursive(n):
    if n <= 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial_recursive(n - 1)


memory = {}
def memoize_factorial(f):
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]
    return inner

@memoize_factorial
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# Let's do some basic testing
print(factorial_iterative_while(4), factorial_recursive(4),   factorial(4), sep="\t")
print(factorial_iterative_while(6), factorial_recursive(6),   factorial(6), sep="\t")
print(factorial_iterative_while(1), factorial_recursive(1),   factorial(1), sep="\t")
print(factorial_iterative_while(0), factorial_recursive(0),   factorial(0), sep="\t")
print(factorial_iterative_while(-7), factorial_recursive(-7), factorial(-7), sep="\t")
print(factorial_iterative_while(5), factorial_recursive(5), factorial(5), sep="\t")
