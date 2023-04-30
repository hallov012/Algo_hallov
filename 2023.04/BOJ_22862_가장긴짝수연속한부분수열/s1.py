import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
cnt = 0
temp = 0
r = 0
for l in range(n):
    while cnt <= k and r < n:
        if nums[r] % 2:
            cnt += 1
        else:
            temp += 1
        r += 1
        if l == 0 and r == n:
            ans = temp
            break

    if cnt == k+1:
        ans = max(ans, temp)
    if nums[l] % 2:
        cnt -= 1
    else:
        temp -= 1
print(ans)
