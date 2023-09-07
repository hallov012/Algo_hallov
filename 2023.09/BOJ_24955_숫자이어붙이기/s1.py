import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def add(data):
    global ans
    ans += data
    ans = str(int(ans) % 1000000007)

n, q = map(int, input().split())
a_lst = [''] + list(input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

p = [-1] * (n+1)
p[1] = 0
stack = [1]
while stack:
    idx = stack.pop()
    for adj in g[idx]:
        if p[adj] == -1:
            p[adj] = idx
            stack.append(adj)

for _ in range(q):
    x, y = map(int, input().split())
    if x == y:
        print(a_lst[x])
        continue
    target_x = [x]
    target_y = [y]
    while p[x]:
        target_x.append(p[x])
        x = p[x]
    while p[y]:
        target_y.append(p[y])
        y = p[y]
    lv_x = len(target_x) - 1
    lv_y = len(target_y) - 1
    while target_x[lv_x] == target_y[lv_y]:
        lv_x -= 1
        lv_y -= 1
    ans = ''
    for i in range(lv_x+1):
        j = target_x[i]
        add(a_lst[j])
    for k in range(lv_y+1, -1, -1):
        t = target_y[k]
        add(a_lst[t])
    print(ans)


