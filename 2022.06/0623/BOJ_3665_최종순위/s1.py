import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    team = list(map(int, input().split()))
    m = int(input())
    g = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    # 기존 등수에 대한 g 그리기
    for i in range(n-1):
        for j in range(i+1, n):
            g[team[i]].append(team[j])
            indegree[team[j]] += 1

    # 변경된 등수 반영
    for _ in range(m):
        a, b = map(int, input().split())
        flag = False
        # a팀이 b팀 보다 등수가 높았을 경우
        for num in g[a]:
            if num == b:
                flag = True
                g[a].remove(b)
                indegree[b] -= 1
                g[b].append(a)
                indegree[a] += 1
                break
        # b팀이 a팀 보다 등수가 높았을 경우
        if not flag:
            g[b].remove(a)
            indegree[a] -= 1
            g[a].append(b)
            indegree[b] += 1

    que = deque()
    ans = []
    for i in range(1, n+1):
        if not indegree[i]:
            que.append(i)

    ans_flag = True
    while que:
        if len(que) != 1:
            ans_flag = False
            break
        v = que.popleft()
        ans.append(v)
        for w in g[v]:
            indegree[w] -= 1
            if not indegree[w]:
                que.append(w)

    if not ans_flag or len(ans) < n:
        print('IMPOSSIBLE')
    else:
        print(*ans)









