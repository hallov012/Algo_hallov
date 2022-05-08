import sys
sys.stdin = open('input.txt')

def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % m
    return temp

def square(adj, n):
    if n == 1:
        return adj
    elif n % 2:
        return multi(square(adj, n-1), adj)
    else:
        return square(multi(adj, adj), n//2)

n = int(input())
m = 1000000007
adj = [[1, 1], [1, 0]]
fibo = [[1], [1]]
if n <= 2:
    print(1)
else:
    print(multi(square(adj, n-2), fibo)[0][0])

"""
행렬을 이용한 피보나치 수 구하기
https://ataraxiady.github.io/dev/2021/04/15/dev-boj-2_11444/
https://www.acmicpc.net/blog/view/28
"""