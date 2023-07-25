import sys
sys.stdin = open('input.txt')

n, m, t, d = map(int, input().split())
arr = []
for _ in range(n):
    data = input().rstrip()
    line = []
    for j in range(m):
        num = ord(data[j])
        if ord(data[j]) <= 90:
            line.append(num-65)
        else:
            line.append(num-71)
