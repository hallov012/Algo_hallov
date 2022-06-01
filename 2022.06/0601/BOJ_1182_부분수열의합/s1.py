import sys
sys.stdin = open('input.txt')

def dfs(sum, idx):
    global ans
    for i in range(idx, n):
        if not visited[i]:
            sum += nums[i]
            visited[i] = 1
            if sum == s:
                ans += 1
            dfs(sum, i)
            sum -= nums[i]
            visited[i] = 0


n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
visited = [0] * (n+1)
dfs(0, 0)
print(ans)
