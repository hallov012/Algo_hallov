import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
ans = 0
s, e = 0, r-1
while s <= e:
    m = (s+e)//2
    dic = defaultdict(int)
    for j in range(c):
        temp = ''
        for i in range(m, r):
            temp += arr[i][j]
        if not dic[temp]:
            dic[temp] += 1
        else:
            break
    if len(dic.keys()) == c:
        ans = m
        s = m + 1
    else:
        e = m - 1

print(ans)