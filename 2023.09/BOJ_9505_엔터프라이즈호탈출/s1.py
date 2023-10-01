import sys, heapq
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    k, w, h = map(int, input().split())
    time = {}
    for _ in range(k):
        name, t = map(str, input().split())
        time[name] = int(t)
    time['E'] = 0
    arr = []
    for i in range(h):
        row = input().rstrip()
        for j in range(w):
            if row[j] == 'E':
                sx, sy = i, j
        arr.append(row)

