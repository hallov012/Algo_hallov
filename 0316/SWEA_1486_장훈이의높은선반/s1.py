import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    ans = b
    for i in range(1, n+1):
        subset = list(combinations(h, i))
        for j in range(len(subset)):
            sum_h = sum(subset[j])
            if sum_h - b >= 0:
                ans = min(sum_h - b, ans)
    print(f'#{tc} {ans}')