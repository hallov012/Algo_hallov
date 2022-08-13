import sys
from itertools import permutations
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
cases = list(permutations(range(1, 9), 8))
ans = 0
for case in cases:
    # 4번 타자는 무조건 0번 선수!
    order = list(case[:3]) + [0] + list(case[3:])
    score = 0
    idx = 0
    for inning in range(n):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out != 3:
            temp = data[inning][order[idx]]
            # 아웃
            if temp == 0:
                out += 1
            elif temp == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif temp == 2:
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1
            elif temp == 3:
                score += b3 + b2 + b1
                b1, b2, b3 = 0, 0, 1
            elif temp == 4:
                score += b3 + b2 + b1 + 1
                b1, b2, b3 = 0, 0, 0
            idx += 1
            if idx == 9:
                idx = 0
    ans = max(ans, score)

print(ans)

