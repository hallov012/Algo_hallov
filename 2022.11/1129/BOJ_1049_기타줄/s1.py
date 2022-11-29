import sys

input = sys.stdin.readline

n, m = map(int, input().split())
box = []
one = []
for _ in range(m):
    a, b = map(int, input().split())
    box.append(a)
    one.append(b)
box.sort()
one.sort()
box_cost = box[0]
one_cost = one[0]
cnt = n
ans = 0
while cnt > 0:
    if cnt <= 6:
        if box_cost > one_cost * cnt:
            ans += one_cost * cnt
        else:
            ans += box_cost
        cnt = 0
    else:
        temp = cnt // 6
        if box_cost > one_cost * 6:
            ans += one_cost * 6 * temp
        else:
            ans += box_cost * temp
        cnt -= 6 * temp
print(ans)