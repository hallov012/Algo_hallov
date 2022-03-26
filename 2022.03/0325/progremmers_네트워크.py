from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = 1
            que = deque([i])
            while que:
                v = que.popleft()
                for w in range(len(computers[v])):
                    if computers[v][w] and not visited[w]:
                        visited[w] = 1
                        que.append(w)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))