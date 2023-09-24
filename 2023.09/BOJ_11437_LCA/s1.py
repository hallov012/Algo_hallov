import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def find_target(i):
    target = [i]
    while p[i] != -1:
        target.append(p[i])
        i = p[i]
    return target, len(target)-1

input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

p = [-1] * (n+1)
p[1] = 0
stack = [1]
while stack:
    v = stack.pop()
    for w in g[v]:
        if p[w] == -1:
            p[w] = v
            stack.append(w)


m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    x_target, x_lv = find_target(x)
    y_target, y_lv = find_target(y)
    while x_target[x_lv] == y_target[y_lv]:
        x_lv -= 1
        y_lv -= 1
    print(x_target[x_lv+1])