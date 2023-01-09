import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    start, end = map(int, input().split())
    n = 10000
    visited = [0] * n
    visited[start] = "."
    que = deque([start])
    counter = {0: "D", 1: "S", 2: "L", 3: "R"}
    while que:
        now = que.popleft()
        if now == end:
            print(visited[now][1:])
            break

        d = (now * 2) % n
        s = (now + 9999) % n
        first = now // 1000
        last = now % 10
        l = (now % 1000) * 10 + first
        r = now // 10 + 1000 * last
        dslr = [d, s, l, r]
        for i in range(4):
            num = dslr[i]
            if not visited[num]:
                visited[num] = visited[now] + counter[i]
                que.append(num)