import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

sum_set = set()
for i in data:
    for j in data:
        sum_set.add(i+j)

ans = {}
for i in data:
    for j in data:
        if (i-j) in sum_set:
            ans[i] = (i, j, i-j)

keys = list(ans.keys())
keys.sort(reverse=True)
print(keys[0])