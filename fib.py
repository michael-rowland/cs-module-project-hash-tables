# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


cache = {}


def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)

    return cache[n]


print(fib(50))


def print_letter_counts(s):
    tally = {}
    s = s.lower()
    for c in s:
        if c == " ":
            continue
        if c not in tally:
            tally[c] = 1
        else:
            tally[c] += 1
    print(sorted([(v, k) for k, v in tally.items()], reverse=True))


print_letter_counts("The quick brown fox jumped over the lazy dog")
print_letter_counts("HELLO WORLD")

