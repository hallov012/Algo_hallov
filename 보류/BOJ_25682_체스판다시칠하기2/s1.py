import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
print(arr)