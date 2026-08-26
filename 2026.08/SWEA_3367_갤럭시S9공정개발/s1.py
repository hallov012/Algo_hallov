import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    files = map(int, input().split())

    add_sum = [0] * (k+1)
    for i in range(k):
        add_sum[i+1] = add_sum[i] + files[i]

    dp = []
