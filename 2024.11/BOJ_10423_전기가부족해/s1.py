import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
power = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]
