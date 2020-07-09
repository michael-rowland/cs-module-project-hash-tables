cache = {}
def expensive_seq(x, y, z):
    # use recursion until BASE CASE of x <= 0
    if x<=0:
        return y + z
    # otherwise, check if in cache, and add if missing
    if (x,y,z) not in cache:
        cache[(x,y,z)] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    # return cached item
    return cache[(x,y,z)]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
