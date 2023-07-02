import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target+1)
    dp[0] = 1
    for c in coin:
        for i in range(1, target+1):
            if i >= c:
                dp[i] += dp[i-c]
    print(dp[target])

