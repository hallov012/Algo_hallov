import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def find(left, right):
    global ans
    if left == right:
        ans = max(ans, nums[left])
        return
    mid = (left + right) // 2
    h = min(nums[mid], nums[mid+1])
    w = 2
    ans = max(ans, h * w)
    i, j = 0, 0
    for _ in range(right-left-1):
        if mid-i == left:
            j += 1
        elif mid+j+1 == right:
            i += 1
        else:
            if nums[mid-i-1] >= nums[mid+j+2]:
                i += 1
            else:
                j += 1
        w += 1
        h = min(h, nums[mid-i], nums[mid+j+1])
        ans = max(ans, h * w)
    find(left, mid)
    find(mid+1, right)

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    else:
        n = nums[0]
        nums = nums[1:]
        ans = 0
        find(0, n-1)
        print(ans)
