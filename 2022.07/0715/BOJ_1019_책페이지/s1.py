import sys
sys.stdin = open('input.txt')

n = int(input())
cnt = [0] * 10
point = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            cnt[int(i)] += point
        n -= 1
    if n < 10:
        for i in range(n+1):
            cnt[i] += point
        cnt[0] -= point
        break
    else:
        for i in range(10):
            cnt[i] += (n//10 + 1) * point
    cnt[0] -= point
    point *= 10
    n //= 10
for i in cnt:
    print(i, end=" ")
