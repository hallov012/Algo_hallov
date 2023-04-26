import sys
sys.stdin = open('input.txt')

def find(idx, cnt):
    if cnt == 6:
        temp = []
        for i in range(n):
            if visited[i]:
                temp.append(nums[i])
        ans.append(temp)
        return
    for i in range(idx+1, n):
        visited[i] = 1
        find(i, cnt+1)
        visited[i] = 0

input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if data == [0]:
        break
    n = data[0]
    nums = sorted(data[1:])
    visited = [0] * n
    ans = []
    find(-1, 0)
    for low in ans:
        print(*low)
    print()