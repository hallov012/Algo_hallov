import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
data.sort()
ans = 0

for i in range(n-2):
    left, right = i+1, n-1
    k = -data[i]
    mx_i = n
    while left < right:
        temp = data[left] + data[right]
        if temp == k:
            if data[left] == data[right]:
                ans += right - left
            else:
                if mx_i > right:
                    mx_i = right
                    while mx_i >= 0 and data[mx_i-1] == data[right]:
                        mx_i -= 1
                ans += right - mx_i + 1
            left += 1
        elif temp < k:
            left += 1
        else:
            right -= 1
print(ans)
