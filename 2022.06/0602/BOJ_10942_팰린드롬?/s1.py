# 팰린드롬 => 회문 (뒤집어 읽어도 처음과 같은 수)
# dp를 사용하여 시간초과 해결하기
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for s in range(n-i):
        e = s + i
        # 한글자라면 무조건 True
        if s == e:
            dp[s][e] = 1
        elif nums[s] == nums[e]:
            # 두글자라면 start와 end 문자가 같다면 무조건 True
            if s + 1 == e:
                dp[s][e] = 1
            # start와 end 사이의 문자가 팰린드롬이라면 해당 문자도 True
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])




