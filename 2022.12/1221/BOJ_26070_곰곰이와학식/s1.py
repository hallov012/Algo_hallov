import sys
sys.stdin = open('input.txt')

x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())
ans = 0
for _ in range(3):
    chicken = min(x1, y1)
    ans += chicken
    x1 -= chicken
    y1 -= chicken
    pizza = min(x2, y2)
    ans += pizza
    x2 -= pizza
    y2 -= pizza
    bugger = min(x3, y3)
    ans += bugger
    x3 -= bugger
    y3 -= bugger
    y2, y3, y1 = y1//3, y2//3, y3//3

print(ans)