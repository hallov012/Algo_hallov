import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
temp = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    temp[a].append(b)
    temp[b].append(a)
virus = [0] * (n + 1)
que = [1]
virus[1] = 1
while que:
    v = que.pop(0)
    for w in temp[v]:
        if not virus[w]:
            virus[w] = 1
            que.append(w)
print(sum(virus) - 1)