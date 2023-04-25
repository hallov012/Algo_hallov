import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        p[x] = y

n = int(input())
m = int(input())
p = list(range(n+1))