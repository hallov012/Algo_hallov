import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
g = [[] for _ in range(n+1)]
for i in range(m):
    lst = list(map(int, input().split()))
    for j in range(2, len(lst)):
        g[lst[j-1]].append(lst[j])
        indegree[lst[j]] += 1

que = deque()
ans = []
for i in range(1, n+1):
    # 그 앞에 선행되어야하는 조건이 없다면 바로 que에 넣는다
    if not indegree[i]:
        que.append(i)
# 일단 먼저 들어가도 되는 애들을 다 넣어두고 que를 돌려야한다
while que:
    v = que.popleft()
    ans.append(v)
    for w in g[v]:
        indegree[w] -= 1
        if not indegree[w]:
            que.append(w)

if len(ans) != n:
    print(0)
else:
    for num in ans:
        print(num)
