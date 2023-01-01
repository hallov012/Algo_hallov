import sys
from itertools import permutations
sys.stdin = open('input.txt')

n, k = map(int, input().split())
w_lst = list(map(int, input().split()))
cases = list(permutations(list(range(n)), n))
ans = 0
for case in cases:
    w = 500
    for i in range(n):
        w += w_lst[case[i]]
        w -= k
        if w < 500:
            break
    else:
        ans += 1

print(ans)