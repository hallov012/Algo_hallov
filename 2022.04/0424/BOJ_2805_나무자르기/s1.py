import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for tree in trees:
        if mid < tree:
            cnt += tree - mid
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)