import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
total = sum(data)
ans = 0
temp = data[0]

# 벌-벌-꿀
# temp는 중간 벌이 못 먹는 꿀의 양
# i는 두번째 벌의 위치
for i in range(1, n):
    temp += data[i]
    ans = max(ans, total - data[0] + total - temp - data[i])

# 꿀-벌-벌
data.reverse()
temp = data[0]
for i in range(1, n):
    temp += data[i]
    ans = max(ans, total - data[0] + total - temp - data[i])

# 벌-꿀-벌
for i in range(1, n):
    ans = max(ans, total - data[0] - data[-1] + data[i])

print(ans)