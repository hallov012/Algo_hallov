import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = []
min_sum = 3000000000

# 첫번째 용액을 선택하는 모든 경우의 수 고려
for i in range(n-2):
    # 두번쨰, 세번째 용액의 idx를 left, right로 저장
    left, right = i + 1, n - 1
    while left < right:
        check = nums[i] + nums[left] + nums[right]
        if abs(check) < min_sum:
            ans = [nums[i], nums[left], nums[right]]
            min_sum = abs(check)
        if check > 0:
            right -= 1
        elif check < 0:
            left += 1
        else:
            break

print(*ans)


