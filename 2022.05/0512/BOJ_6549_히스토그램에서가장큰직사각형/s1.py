import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def find(data):
    n = len(data)
    if n == 1:
        return data[0]
    if n % 2:
        data = [0] + data
    mid = n // 2
    height = min(data[mid-1], data[mid])
    left = data[:mid]
    right = data[mid:]
    width = 2
    area = height * width
    i, j = 0, 0  # i는 왼쪽으로, j는 오른쪽으로 이동
    for _ in range(n-2):
        if mid - i - 1 == 0:
            j += 1
        elif mid + j == n - 1:
            i += 1
        else:
            if data[mid - i - 2] >= data[mid + j + 1]:
                i += 1
            else:
                j += 1
        height = min(height, data[mid - 1 - i], data[mid + j])
        width += 1
        area = max(area, height * width)
    return max(find(left), find(right), area)

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    ans = find(nums)
    print(ans)