from itertools import combinations

def solution(numbers):
    answer = 0
    m = len(numbers)
    n = 10 ** m
    decimal = [1] * (n+1)
    decimal[0], decimal[1] = 0, 0
    for i in range(2, n+1):
        if decimal[i]:
            for j in range(2*i, n+1, i):
                decimal[j] = 0
    visited = [0] * m
    def dfs(cnt, ans):
        nonlocal answer
        if ans != '' and decimal[int(ans)]:
            answer += 1
            decimal[int(ans)] = 0
        for i in range(m):
            if not visited[i]:
                visited[i] = 1
                dfs(cnt+1, ans+numbers[i])
                visited[i] = 0
    dfs(0, '')
    return answer

print(solution("17"))
print(solution("011"))