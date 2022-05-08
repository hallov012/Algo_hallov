import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
cnt = [0] * m
ans = 0
for i in range(n+1):
    nums[i] += nums[i-1]
    # 처음부터 i번째 숫자까지 모두 더한 합의 나머지를 cnt로 세어준다
    cnt[nums[i] % m] += 1

# 나머지가 같은 애들 중 2개씩 뽑은 모든 경우의 합이 ans 값이 된다
for i in range(m):
    if cnt[i]:
        ans += cnt[i] * (cnt[i]-1) // 2
print(ans)