import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
know = list(map(int, input().split()))
que = deque(know[1:])
know_pepole = [0] * (n+1)
for i in range(1, len(know)):
    know_pepole[know[i]] += 1
# 진실을 아는 사람이 참석하는 파티에는 무조건 진실을 말해야한다
# 진실을 말한 파티에 참석한 사람이 있는 파티에는 무조건 진실을 말해야한다
pepole = defaultdict(list)
parties = []
for i in range(m):
    party = list(map(int, input().split()))
    parties.append(party[1:])
    for person in party[1:]:
        pepole[person].append(i)

ans = [1] * m
while que:
    v = que.popleft()
    for p in pepole[v]:
        if ans[p]:
            ans[p] = 0
        for person in parties[p]:
            if not know_pepole[person]:
                know_pepole[person] += 1
                que.append(person)

print(sum(ans))

