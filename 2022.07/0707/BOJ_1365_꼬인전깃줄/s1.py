import sys
sys.stdin = open('input.txt')

def binary(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

input = sys.stdin.readline

# 증가하는 부분수열이 있으면 그 구간의 선끼리는 꼬이지 않음
n = int(input())
data = list(map(int, input().split()))
lis = [data[0]]
for i in range(1, n):
    if lis[-1] < data[i]:
        lis.append(data[i])
    else:
        idx = binary(0, len(lis)-1, data[i])
        lis[idx] = data[i]
print(n-len(lis))


