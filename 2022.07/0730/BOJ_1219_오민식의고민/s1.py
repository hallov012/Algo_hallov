import sys
sys.stdin = open('input.txt')

def dfs(next):
    visited = [0] * n
    q = [next]
    while q:
        x = q.pop()
        # next에서 시작해 end로 돌아갈 수 있는 경우 계속 이익을 얻으며 돌 수 있음
        if x == end:
            return True
        visited[x] = 1
        for b, c in edges[x]:
            if not visited[b]:
                q.append(b)
    return False

def bellman_ford():
    dist[start] = gain[start]
    for i in range(n+1):
        # end에 방문하지 못하는 경우
        if dist[end] == -sys.maxsize and i == n:
            print('gg')
            return False
        for now in range(n):
            for next, ni in edges[now]:
                if dist[now] != -sys.maxsize and dist[next] < dist[now] + ni:
                    dist[next] = dist[now] + ni
                    if i == n:
                        if dfs(next):
                            print('Gee')
                            return False
    return True


input = sys.stdin.readline

n, start, end, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
gain = list(map(int, input().split()))

dist = [-sys.maxsize] * n
# edges의 cost를 gain-cost로 바꾸기
for i in range(n):
    for j in range(len(edges[i])):
        for k in range(n):
            if edges[i][j][0] == k:
                edges[i][j][1] = gain[k] - edges[i][j][1]

if bellman_ford():
    print(dist[end])