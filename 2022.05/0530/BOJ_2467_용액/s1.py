import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))

ans = []
min_sum = 2000000000
left, right = 0, n-1
while left < right:
    check = nums[left] + nums[right]
    # 최솟값이 갱신됐을 때, min_sum과 ans를 갱신
    if abs(check) < min_sum:
        ans = [nums[left], nums[right]]
        min_sum = abs(check)
    # 합이 양수라면 더 작은 수를 골라와야 하므로 right를 줄여주는 것이 좋다
    if check > 0:
        right -= 1
    # 합이 음수라면 더 큰 수를 골라와야 하므로 left를 늘려주는 것이 좋다
    elif check < 0:
        left += 1
    # check = 0 이라면 이보다 작은 값이 나올 수 없으므로 종료
    else:
        break

print(*ans)
