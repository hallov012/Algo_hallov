# 밸만포드 알고리즘 https://velog.io/@kimdukbae/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Bellman-Ford-Algorithm

import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def bellman_ford(start):
    distance[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for e, d in roads[s]:
                if distance[s] + d < distance[e]:
                    distance[e] = distance[s] + d
                    if i == n:  # n-1번 이후에도 값이 갱신된 경우
                        return True
    return False

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n, m, w = map(int, input().split())
    roads = defaultdict(list)
    for _ in range(m):
        s, e, t = map(int, input().split())
        roads[s].append((e, t))
        roads[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        roads[s].append((e, -t))
    inf = 987654321
    distance = [inf] * (n+1)
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")



