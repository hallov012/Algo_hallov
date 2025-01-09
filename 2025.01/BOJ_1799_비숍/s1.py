import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(num, cnt):
    global ans
    if num == n * n:
        ans = max(ans, cnt)
        return
    x, y = num // n, num % n
    flag = True
    if not arr[x][y]:
        flag = False
    # upper 체크
    if upper_visited[x+y]:
        flag = False
    # down 체크
    if down_visited[x-y]:
        flag = False

    if flag:
        upper_visited[x+y] = 1
        down_visited[x-y] = 1
        find(num + 1, cnt + 1)
        upper_visited[x+y] = 0
        down_visited[x-y] = 0
    find(num + 1, cnt)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = 2 * n
upper_visited = defaultdict(int)
down_visited = defaultdict(int)

ans = 0
find(0, 0)

print(ans)


