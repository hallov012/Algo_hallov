import sys, math
sys.stdin = open('input.txt')

pa = int(input()) / 100
pb = int(input()) / 100
# 소수가 아닌 경우로 득점
# 1에서 둘 다 소수가 아닌 점수를 득점하는 결과를 출력
score = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
a_percent = {}
for num in score:
    temp = math.comb(18, num) * (pa ** num) * ((1 - pa) ** (18 - num))
    a_percent[num] = temp

b_percent = {}
for num in score:
    temp = math.comb(18, num) * (pb ** num) * ((1 - pb) ** (18 - num))
    b_percent[num] = temp

ans = 0
for n1, p1 in a_percent.items():
    for n2, p2 in b_percent.items():
        ans += p1 * p2

print(1-ans)
