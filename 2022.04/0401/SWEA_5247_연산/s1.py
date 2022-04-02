import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    max_num = 10 ** 6
    visited = [0] * (max_num + 1)
    que = deque([n])
    visited[n] = 1
    while que:
        num = que.popleft()
        if num == m:
            break
        if num + 1 <= max_num and not visited[num + 1]:
            visited[num + 1] = visited[num] + 1
            que.append(num + 1)
        if num - 1 > 0 and not visited[num - 1]:
            visited[num - 1] = visited[num] + 1
            que.append(num - 1)
        if 2 * num <= max_num and not visited[2 * num]:
            visited[2 * num] = visited[num] + 1
            que.append(2 * num)
        if num - 10 > 0 and not visited[num - 10]:
            visited[num - 10] = visited[num] + 1
            que.append(num - 10)
    ans = visited[m] - 1
    print(f'#{tc} {ans}')
