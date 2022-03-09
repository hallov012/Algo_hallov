import sys
from collections import deque
sys.stdin = open('input.txt')

for tc in range(1, 10+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for j in range(n):
        col = deque([])
        for i in range(n):
            if data[i][j] != 0:
                col.append(data[i][j])
        if not len(col):
            break
        else:
            if col[0] == 2:
                col.popleft()
            if col[-1] == 1:
                col.pop()
            for a in range(len(col)-1):
                if col[a] == 1 and col[a+1] == 2:
                    cnt += 1
    print(f'#{tc} {cnt}')





