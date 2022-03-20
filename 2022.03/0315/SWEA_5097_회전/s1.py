import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(m):
        num = nums.pop(0)
        nums.append(num)
    print(f'#{tc} {nums[0]}')