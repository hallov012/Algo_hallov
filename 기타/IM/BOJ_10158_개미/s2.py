import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
if (p + t) % (2 * w) > w:
    ans_p = 2 * w - ((p + t) % (2 * w))
else:
    ans_p = (p + t) % (2 * w)
if (q + t) % (2 * h) > h:
    ans_q = 2 * h - ((q + t) % (2 * h))
else:
    ans_q = (q + t) % (2 * h)
print(ans_p, ans_q)