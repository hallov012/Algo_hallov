import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, q = map(int, input().split())
a_lst = [''] + list(input().split())
# 부모 노드 저장
p = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    p[b] = a

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
        ans += a_lst[j]
    for k in range(lv_y+1, -1, -1):
        t = target_y[k]
        ans += a_lst[t]
    print(int(ans) % 1000000007)


