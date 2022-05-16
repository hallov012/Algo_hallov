import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

c = int(input())

for tc in range(c):
    d, n = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    check = [0] * (n+1)
    cnt = [0] * d
    cnt[0] = 1
    ans = 0
    for i in range(1, n+1):
        nums[i] += nums[i-1]
        check[i] = nums[i]
        cnt[nums[i] % d] += 1
    for num in cnt:
        if num >= 2:
            ans += num * (num-1) // 2
    print(ans)

