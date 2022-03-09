import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * 10
    nums.sort()
    for i in range(5):
        ans[2*i] = nums[n-i-1]
        ans[2*i+1] = nums[i]
    print(f'#{tc}', end=" ")
    print(*ans)
