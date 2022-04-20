import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

word1 = input().strip()
word2 = input()
n, m = len(word1), len(word2)
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if word1[j-1] == word2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
print(dp)