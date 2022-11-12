import sys
sys.stdin = open('input.txt')

n = int(input())
g = [input().rstrip() for _ in range(n)]
edges = []
# for i in range(n-1):
#     for j in range(i+1, n):
#