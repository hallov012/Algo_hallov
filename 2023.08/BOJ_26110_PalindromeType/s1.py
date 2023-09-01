import sys
sys.stdin = open('input.txt')

# 최대 3개의 문자를 제거해서 펠린드롬으로 만들기
word = input()
reverse = word[::-1]
print(word, reverse)
if word == reverse:
    print(0)
    exit()

n = len(word)
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if word[i-1] == reverse[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for line in dp:
    print(line)

ans = n - dp[n][n]
if ans > 3:
    print(-1)
else:
    print(ans)


