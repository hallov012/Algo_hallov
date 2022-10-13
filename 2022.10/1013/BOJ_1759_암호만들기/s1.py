import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(num, cnt, idx, arr, dic):
    if cnt == num:
        temp = []
        for i in range(len(arr)):
            if visited[i]:
                temp.append(arr[i])
        dic[num].append(temp)
    for i in range(idx+1, len(arr)):
        if not visited[i]:
            visited[i] = 1
            dfs(num, cnt+1, i, arr, dic)
            visited[i] = 0

input = sys.stdin.readline

l, c = map(int, input().split())
chars = list(map(str, input().split()))
coll = []
cons = []
ans = []
for char in chars:
    if char in "aeiou":
        coll.append(char)
    else:
        cons.append(char)

coll_dict = defaultdict(list)
for i in range(1, l-1):
    visited = [0] * len(coll)
    dfs(i, 0, -1, coll, coll_dict)

cons_dict = defaultdict(list)
for i in range(2, l):
    visited = [0] * len(cons)
    dfs(i, 0, -1, cons, cons_dict)

for i in range(1, l-1):
    for first in coll_dict[i]:
        for second in cons_dict[l-i]:
            temp = first + second
            temp.sort()
            ans.append("".join(temp))
ans.sort()
for word in ans:
    print(word)

