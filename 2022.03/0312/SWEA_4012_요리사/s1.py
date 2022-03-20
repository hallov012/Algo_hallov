import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    food = list(range(n))
    m = n // 2
    sub_set = []
    ans = 100
    food_a = list(combinations(food, m))
    for a in food_a:
        if len(a) == 2:
            taste_a = synergy[a[0]][a[1]] + synergy[a[1]][a[0]]
        else:
            a_sub = list(combinations(a, 2))
            taste_a = 0
            for sub in a_sub:
                taste_a += synergy[sub[0]][sub[1]] + synergy[sub[1]][sub[0]]
        b = list(set(food) - set(a))
        if len(b) == 2:
            taste_b = synergy[b[0]][b[1]] + synergy[b[1]][b[0]]
        else:
            b_sub = list(combinations(b, 2))
            taste_b = 0
            for sub in b_sub:
                taste_b += synergy[sub[0]][sub[1]] + synergy[sub[1]][sub[0]]
        gap = abs(taste_a - taste_b)
        ans = min(ans, gap)
    print(f'#{tc} {ans}')
