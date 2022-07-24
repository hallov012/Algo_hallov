import sys
sys.stdin = open('input.txt')

n = int(input())
k = int(input())
if n > 100:
    m = n // 100
else:
    m = n
num = m * 100
min_ans = k
ans = []
for i in range(10):
    for j in range(10):
        temp = num + 10*i + j
        if temp % k < min_ans:
            min_ans = temp % k
            ans = [i, j]

ans = list(map(str, ans))
print("".join(ans))

