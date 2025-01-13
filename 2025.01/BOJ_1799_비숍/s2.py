"""
시간 초과 해결을 위해 white, black 칸으로 나누어서 진행
"""
import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(num, cnt, white_black_flag):
    global ans_white, ans_black
    if num >= n * n:
        if white_black_flag:
            ans_white = max(ans_white, cnt)
        else:
            ans_black = max(ans_black, cnt)
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
        find(num + 2, cnt + 1, white_black_flag)
        upper_visited[x+y] = 0
        down_visited[x-y] = 0
    find(num + 2, cnt, white_black_flag)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans_white, ans_black = 0, 0

upper_visited = defaultdict(int)
down_visited = defaultdict(int)
find(0, 0, True)
find(1, 0, False)

print(ans_white + ans_black)


