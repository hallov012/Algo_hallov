import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    i = 2
    ans = 0
    while i < n - 2:
        if height[i-2] < height[i] and height[i-1] < height[i] and height[i+1] < height[i] and height[i+2] < height[i]:
            ans += height[i] - max([height[i-2], height[i-1], height[i+1], height[i+2]])
            i += 3
        else:
            i += 1
    print(f'#{tc} {ans}')
