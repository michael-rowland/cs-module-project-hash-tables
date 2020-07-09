# Your code here
import math, random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

storage = {}
for x in range(2, 14):
    for y in range(3, 6):
        storage[f'{x}{y}'] = slowfun_too_slow(x,y)

def slowfun(x, y, storage=storage):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    return storage[f'{x}{y}']


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
