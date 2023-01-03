import sys
from itertools import combinations
sys.stdin = open('input.txt')

s = input().rstrip()
n = len(s)
stack = []
check = [0] * n
idx = 1
for i in range(n):
    char = s[i]
    if char == '(':
        stack.append(i)
    elif char == ')':
        j = stack.pop()
        check[j] = idx
        check[i] = idx
        idx += 1

ans = set()
for i in range(1, idx):
    cases = combinations(list(range(1, idx)), i)
    for case in cases:
        temp = ""
        for j in range(n):
            if check[j] not in case:
                temp += s[j]
        ans.add(temp)

for str in sorted(list(ans)):
    print(str)

