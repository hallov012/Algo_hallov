import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = max(nums) - min(nums)
    print(f'#{tc} {ans}')