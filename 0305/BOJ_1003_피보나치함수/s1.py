import sys
sys.stdin = open('input.txt')

def fibo_sum(n):
    global ans
    if n == 0:
        ans[0] += 1
        return
    if n == 1:
        ans[1] += 1
        return
    fibo_sum(n-1)
    fibo_sum(n-2)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ans = [0, 0]
    fibo_sum(n)
    print(*ans)
