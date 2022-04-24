import sys
sys.stdin = open('input.txt')

def prim():
    for _ in range(V):
        min_idx = -1
        min_value = inf
        # 최솟값 찾기
        for i in range(V + 1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1
        # 해당 값으로부터 연결된 정점 가중치 갱신
        for i in range(V + 1):
            if not visited[i] and g[min_idx][i] < key[i]:
                key[i] = g[min_idx][i]
    print(key)
    return sum(key)


V, E = map(int, input().split())
inf = 987654321
g = [[inf] * (V + 1) for _ in range(V + 1)]
key = [inf] * (V + 1)
key[2] = 0
visited = [0] * (V + 1)
for i in range(E):
    s, e, w = map(int, input().split())
    g[s][e] = w
    g[e][s] = w
print(prim())