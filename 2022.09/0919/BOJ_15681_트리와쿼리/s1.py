import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def find(x):
    cnt[x] = 1
    for i in tree[x]:
        if not cnt[i]:
            find(i)
            cnt[x] += cnt[i]

input = sys.stdin.readline

n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
cnt = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

find(r)

for _ in range(q):
    u = int(input())
    print(cnt[u])