import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def dfs(x):
    cnt = 0
    for i in tree[x]:
        cnt += dfs(i)

    if woolf[x]:
        cnt -= woolf[x]
        if cnt < 0:
            cnt = 0
    else:
        cnt += sheep[x]
    return cnt

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
sheep = [0] * (n+1)
woolf = [0] * (n+1)
for i in range(2, n+1):
    t, a, p = input().split()
    tree[int(p)].append(i)
    if t == 'S':
        sheep[i] = int(a)
    else:
        woolf[i] = int(a)

print(dfs(1))
