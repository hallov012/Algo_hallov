import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

"""
양이 7의 배수면 민초 => 먹으면 순서를 뒤집음
"""
input = sys.stdin.readline

n, m = map(int, input().split())
a_lst = list(map(int, input().split()))
data = defaultdict(deque)

for i in range(1, n+1):
    a = a_lst[i-1]
    data[a].append(i)

lst = data.items()
lst = sorted(lst)
rev = 0
for _ in range(m):
    f, idxs = lst[-1]
    if len(idxs) == 1:
        print(idxs[0])
        lst.pop()
    else:
        # 오른쪽에서부터 먹을 때
        if rev:
            print(lst[-1][1].pop())
        else:
            print(lst[-1][1].popleft())
    if not f % 7:
        rev = abs(rev - 1)




