import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
x = int(input())
data.sort()
left, right = 0, n-1
ans = 0
while left < right:
    temp = data[left] + data[right]
    if temp == x:
        ans += 1
        right -= 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(ans)