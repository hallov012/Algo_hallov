import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    ans = [sys.maxsize, 0]
    for i in range(n):
        left, right = i+1, n-1
        while left <= right:
            mid = (left+right)//2
            temp = data[i] + data[mid]
            if temp > k:
                right = mid - 1
            else:
                left = mid + 1
            if abs(temp-k) < ans[0]:
                ans[0], ans[1] = abs(temp-k), 1
            elif abs(temp-k) == ans[0]:
                ans[1] += 1
    print(ans[1])