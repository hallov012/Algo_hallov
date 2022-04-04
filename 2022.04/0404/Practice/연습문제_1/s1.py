def make_set(x):
    p[x] = x

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    x, y = find_set(x), find_set(y)
    p[find_set(y)] = find_set(x)

p = list(range(7))
print(p)
print('--------------')

union(1, 3)
print(p)
print('--------------')

union(2, 3)
print(p)
print('--------------')

union(5, 6)
print(p)
print('--------------')

print(find_set(6))  # 6 -> 5
print(find_set(3))  # 3 -> 1 -> 2
print(find_set(2))  # 3 -> 1 -> 2
