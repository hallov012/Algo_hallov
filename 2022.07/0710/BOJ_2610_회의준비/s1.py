"""
플로이드 워셜(Floyd Warshall)로 최단경로를 찾는다
https://freedeveloper.tistory.com/385
"""
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            dist[a][b] = min(dist[a][b], dist[a][i] + dist[i][b])

check = [0] * (n+1)
team_lst = []
for i in range(1, n+1):
    if not check[i]:
        team = []
        for j in range(1, n+1):
            if dist[i][j] != sys.maxsize:
                check[j] = 1
                team.append(j)
        team_lst.append(team)

ans = []
for team in team_lst:
    leader = [0, sys.maxsize]
    for i in range(len(team)):
        max_cnt = 0
        for j in range(len(team)):
            max_cnt = max(max_cnt, dist[team[i]][team[j]])
        if max_cnt < leader[1]:
            leader = [team[i], max_cnt]
    ans.append(leader)
ans.sort()

print(len(ans))
for idx, cnt in ans:
    print(idx)
