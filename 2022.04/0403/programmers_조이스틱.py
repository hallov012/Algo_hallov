def solution(name):
    def dfs(move, idx):
        nonlocal move_cnt
        if move >= move_cnt:
            return
        if 0 not in visited:
            move_cnt = move
            return
        visited[idx + 1] += 1
        dfs(move + 1, idx + 1)
        visited[idx + 1] -= 1
        visited[idx - 1] += 1
        dfs(move + 1, idx - 1)
        visited[idx - 1] -= 1

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(name)
    m = len(alphabet)
    answer = m * n
    cnt = [0] * n
    for i in range(n):
        char = name[i]
        if alphabet.index(char) <= m // 2:
            cnt[i] = alphabet.index(char)
        else:
            cnt[i] = m - alphabet.index(char)
    visited = [0] * n
    visited[0] = 1
    for j in range(n):
        if not cnt[j]:
            visited[j] = 1
    move_cnt = n * m
    dfs(0, 0)
    answer = sum(cnt) + move_cnt
    return answer

print(solution("JEROEN"))
print(solution("JAN"))