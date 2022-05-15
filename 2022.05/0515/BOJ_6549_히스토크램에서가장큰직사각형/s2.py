import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

def find(left, right):
    global ans
    if left == right:
        return
    mid = (left + right) // 2
    h = min(nums[mid-1], nums[mid])
    w = 2
    for i in range(mid-2, -1, -1):
        if nums[i] >= h:
            w += 1
        else:
            break
    for j in range(mid+1, n):
        if nums[j] >= h:
            w += 1
        else:
            break
    ans = max(ans, h * w)
    find(left, mid)
    find(mid+1, right)

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    else:
        n = len(nums)
        ans = 0
        find(0, n-1)
        print(ans)