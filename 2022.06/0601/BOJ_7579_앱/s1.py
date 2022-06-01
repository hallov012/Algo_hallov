# https://claude-u.tistory.com/445
# 냅색 알고리즘
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
a_lst = [0] + list(map(int, input().split()))
c_lst = [0] + list(map(int, input().split()))
dp = [[0] * (sum(c_lst) + 1) for _ in range(n+1)]
result = sum(c_lst)

for i in range(1, n+1):
    byte = a_lst[i]
    cost = c_lst[i]
    for j in range(1, result + 1):
        if j < cost: # 앱을 비활성화 할 만큼의 cost가 충분치 않음
            dp[i][j] = dp[i-1][j]
        else: # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 경우의 byte 비교
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
        if dp[i][j] >= m: # 조건 충족
            result = min(result, j)
if m != 0:
    print(result)
else:
    print(0)