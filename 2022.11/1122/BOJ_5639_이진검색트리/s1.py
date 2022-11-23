import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt')

input = sys.stdin.readline

nums = []
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break

def postorder(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first+1, end+1):
        if nums[first] < nums[i]:
            mid = i
            break
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(nums[first])

postorder(0, len(nums)-1)