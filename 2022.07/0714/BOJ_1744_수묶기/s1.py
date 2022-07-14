import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
positive = []
negative = []
ans = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        ans += 1
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

# 양수 더하기
if len(positive) % 2:
    for i in range(0, len(positive)-1, 2):
        ans += positive[i] * positive[i+1]
    ans += positive[len(positive) - 1]
else:
    for i in range(0, len(positive), 2):
        ans += positive[i] * positive[i+1]

# 음수 더하기
if len(negative) % 2:
    for i in range(0, len(negative)-1, 2):
        ans += negative[i] * negative[i+1]
    ans += negative[len(negative)-1]
else:
    for i in range(0, len(negative), 2):
        ans += negative[i] * negative[i+1]

print(ans)
