from collections import deque

def solution(n, edge):
    g = [[] for _ in range(n + 1)]
    for start, end in edge:
        g[start].append(end)
        g[end].append(start)
    visited = [0] * (n + 1)
    visited[1] = 1
    que = deque([1])
    while que:
        v = que.popleft()
        for w in g[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                que.append(w)
    answer = 0
    for i in range(n + 1):
        if visited[i] == max(visited):
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))