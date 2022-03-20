import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

data = [[0] * (n+1)]
for _ in range(n):
    data.append([0] + list(map(int, input().split())))
quests = [list(map(int, input().split())) for _ in range(m)]

for i in range(n+1):
    for j in range(1, n+1):
        data[i][j] += data[i][j-1]
for i in range(1, n+1):
    for j in range(n+1):
        data[i][j] += data[i-1][j]

for quest in quests:
    x1, y1, x2, y2 = quest[0], quest[1], quest[2], quest[3]
    ans = data[x2][y2] - data[x1-1][y2] - data[x2][y1-1] + data[x1-1][y1-1]
    print(ans)