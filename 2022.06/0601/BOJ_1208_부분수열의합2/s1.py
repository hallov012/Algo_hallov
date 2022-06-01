import sys
sys.stdin = open('input.txt')

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
sum = nums[0]
ans = 0

while True:
    # 값이 더 클 고려해야할 사항..
    # 만약 sum이 음수일 때, sum < s라면 right를 nums[right]이 양수일 때 까지 늘려주자
    if sum >= s:
        if sum == s:
            ans += 1
        sum -= nums[left]
        left += 1
    elif right >= n:
        break
    else:
        if nums[right] < 0:
            while nums[right] < 0:
                right += 1
                sum += nums[right]
        elif nums[left] < 0:
            sum -= nums[left]
            left += 1
        else:
            right += 1
            sum += nums[right]
print(ans)
