def fib(max):
    a, b = 1, 1
    while b < max:
        yield b
        a, b = b, a + b
    return

print(sum([x for x in fib(4000000) if x % 2 == 0]))
