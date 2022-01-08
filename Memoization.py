"""
Memoization is a technique of recording the intermediate results so that it can be use to
avoid repeated calculations and speed up the programs. In python it can be done using function decorators.
Memoization can be used to optimize the programs that use recursion.
"""
# Simple recursive program to find factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))

# The previous program can be optimized by memoization using decorators
def memoize_factorial(f):
    memory = {}
    # This inner function has access to memory and to 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
    return inner

@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)
print(facto(5))