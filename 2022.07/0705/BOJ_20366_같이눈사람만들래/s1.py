import sys
sys.stdin = open('input.txt')

n = int(input())
size = list(map(int, input().split()))
size.sort()
ans = sys.maxsize
# 모든 사이즈에 대해서 투포인터탐색 진행
for i in range(n):
    for j in range(i+3, n):
        left, right = i+1, j-1
        while left < right:
            temp = (size[i] + size[j]) - (size[left] + size[right])
            if ans > abs(temp):
                ans = abs(temp)
            if temp < 0:
                right -= 1
            else:
                left += 1
print(ans)