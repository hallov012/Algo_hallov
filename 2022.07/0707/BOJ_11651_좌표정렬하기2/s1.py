import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((y, x))
data.sort()
for sub in data:
    print(sub[1], sub[0])
