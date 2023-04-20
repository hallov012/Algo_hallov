import sys
sys.stdin = open('input.txt')

code = '0' + input()
if code[1] == '0':
    print(0)
    exit()

n = len(code)
m = 1000000
dp = [0] * n
dp[0] = dp[1] = 1
for i in range(1, n):
    if code[i] != '0':
        dp[i] = dp[i-1]
    temp = code[i-1] + code[i]
    if 10 <= int(temp) <= 26:
        dp[i] += dp[i-2]
print(dp[-1] % m)

