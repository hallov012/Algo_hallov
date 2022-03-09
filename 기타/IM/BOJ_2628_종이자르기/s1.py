import sys
sys.stdin = open('input.txt')

w, l = map(int, input().split())
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
a_cut, b_cut = [0], [0]  # a 가로로 자르는 것, b 세로로 자르는 것
for i in range(n):
    if data[i][0]:
        b_cut.append(data[i][1])
    else:
        a_cut.append(data[i][1])
a_cut.sort()
a_cut.append(l)
b_cut.sort()
b_cut.append(w)
l_lst, w_lst = [], []
for i in range(1, len(a_cut)):
    l_lst.append(a_cut[i] - a_cut[i-1])
for i in range(1, len(b_cut)):
    w_lst.append(b_cut[i] - b_cut[i-1])

ans = 0
for l in l_lst:
    for w in w_lst:
        if l * w > ans:
            ans = l * w
print(ans)

