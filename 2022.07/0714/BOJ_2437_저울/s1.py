import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
data.sort()

# 현재까지 나온 추의 합 + 1과 추의 무게를 비교
# 만약 현재까지 나온 추의 합 + 1이 추의 무게보다 작으면 그 수는 구현할 수 없음
ans = 0
for i in range(n):
    if ans + 1 >= data[i]:
        ans += data[i]
    else:
        break

print(ans+1)