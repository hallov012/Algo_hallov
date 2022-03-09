import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    t, N = input().split()
    n = int(N)
    data = list(map(str, input().split()))
    num1 = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0] * 10
    for i in data:
        cnt[num1.index(i)] += 1
    print(t)
    for i in range(10):
        for j in range(cnt[i]):
            print(num1[i], end=" ")
    print()

