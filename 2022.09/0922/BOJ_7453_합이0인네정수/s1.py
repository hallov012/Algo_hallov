import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
a_lst, b_lst, c_lst, d_lst = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)
    c_lst.append(c)
    d_lst.append(d)


ab_dict, cd_dict = defaultdict(int), defaultdict(int)
ans = 0
for a in a_lst:
    for b in b_lst:
        ab_dict[a+b] += 1
for c in c_lst:
    for d in d_lst:
        if -(c+d) in ab_dict.keys():
            ans += ab_dict[-(c+d)]
print(ans)
