"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

def f(x):
    return x * 4 + 6

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)    
qa = tuple(f(i) for i in q)

sums = {}
diffs = {}

# generates a list of all sums and diffs for q
for i, a in zip(q, qa):
    for j, b in zip(q, qa):
        if a+b not in sums:
            sums[a+b] = []
        sums[a+b].append((i, j, a, b))
        if a-b not in diffs:
            diffs[a-b] = []
        diffs[a-b].append((i, j, a, b))

for sum_ in sums:
    # if this is true, we know the values of q in 
    if sum_ in diffs:
        # loop through matches in sums dictionary
        for s_pair in sums[sum_]:
            # loop through matches in diffs dictionary
            for d_pair in diffs[sum_]:
                print(f'f({s_pair[0]}) + f({s_pair[1]}) = f({d_pair[0]}) - f({d_pair[1]})\t{s_pair[2]} + {s_pair[3]} = {d_pair[2]} - {d_pair[3]}')