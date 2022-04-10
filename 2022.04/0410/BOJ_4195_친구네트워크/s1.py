import sys
sys.stdin = open('input.txt')

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    elif x < y:
        p[y] = x
        size[x] += size[y]
    else:
        p[x] = y
        size[y] += size[x]

input = sys.stdin.readline

t = int(input())
for tc in range(t):
    f = int(input())
    name_dict = {}
    p = [0]
    size = [1]
    cnt = 0
    for _ in range(f):
        a, b = map(str, input().split())
        if a not in name_dict.keys():
            cnt += 1
            name_dict[a] = cnt
            p.append(cnt)
            size.append(1)
        if b not in name_dict.keys():
            cnt += 1
            name_dict[b] = cnt
            p.append(cnt)
            size.append(1)
        x, y = name_dict[a], name_dict[b]
        union(x, y)
        print(size[find(x)])