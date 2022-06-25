import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

# 가능하면 쉬운 문제부터 풀어야 한다는 것이 포인트 => 최소힙으로 낮은 난이도부터 꺼내준다
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    indegree[b] += 1

q = []
ans  = []
for i in range(1, n+1):
    if not indegree[i]:
        heapq.heappush(q, i)

while q:
    v = heapq.heappop(q)
    ans.append(v)
    for w in g[v]:
        indegree[w] -= 1
        if not indegree[w]:
            heapq.heappush(q, w)

print(*ans)