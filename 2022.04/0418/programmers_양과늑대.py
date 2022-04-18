def solution(info, edges):
    answer = 0
    n = len(info)
    g = [[0] * 2 for _ in range(n)]
    for edge in edges:
        s, e = edge
        if g[s][0] == 0:
            g[s][0] = e
        else:
            g[s][1] = e
    now_go = [0] * n
    if g[0][0] != 0:
        now_go[g[0][0]] = 1
    if g[0][1] != 0:
        now_go[g[0][1]] = 1
    visited = [0] * n
    visited[0] = 1
    def dfs(now, sheep, wolf):
        nonlocal answer
        if sheep <= wolf:
            return
        answer = max(answer, sheep)
        for i in range(n):
            if now_go[i]:
                now_go[i] = 0
                visited[i] = 1
                if info[i]:
                    sheep_plus = 0
                    wolf_plus = 1
                else:
                    sheep_plus = 1
                    wolf_plus = 0
                a, b = 0, 0
                if g[i][0] != 0 and not visited[g[i][0]]:
                    a = 1
                if g[i][1] != 0 and not visited[g[i][1]]:
                    b = 1
                now_go[g[i][0]] += a
                now_go[g[i][1]] += b
                dfs(i, sheep+sheep_plus, wolf+wolf_plus)
                now_go[i] = 1
                visited[i] = 0
                now_go[g[i][0]] -= a
                now_go[g[i][1]] -= b
    dfs(0, 1, 0)
    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
