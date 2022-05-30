import sys, math
sys.stdin = open('input.txt')

m = 4000000

# 에라토스테네스의 체
nums = [1] * (m+1)
nums[0], nums[1] = 0, 0
for i in range(2, int(math.sqrt(m)+1)):
    if nums[i]:
        for j in range(2*i, m+1, i):
            nums[j] = 0

n = int(input())
ans = 0
left, right = 2, 2
sum = 2
while True:
    if sum >= n:
        if sum == n:
            ans += 1
        sum -= left
        left += 1
        while not nums[left]:
            left += 1
            if left > n:
                break
    elif right > n:
        break
    else:
        flag = True
        right += 1
        while not nums[right]:
            right += 1
            if right > n:
                flag = False
                break
        if flag:
            sum += right

print(ans)