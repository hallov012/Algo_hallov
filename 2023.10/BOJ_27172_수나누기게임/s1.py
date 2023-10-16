import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

result = [-1] * (sorted_nums[-1] + 1)
for k in nums:
    result[k] = 0

# 자신의 숫자가 상대의 약수이면 승리
# 반대로 상대의 숫자가 자신의 약수이면 패배
for i in range(n-1):
    num = sorted_nums[i]
    for j in range(2, sorted_nums[-1]//num + 1):
        # num의 배수가 있었다면 이길 수 있다는 것 :)
        if result[num * j] >= 0:
            result[num * j] += 1
            result[num] -= 1

for i in range(n):
    print(-1 * result[nums[i]], end=" " if i != n-1 else "")


