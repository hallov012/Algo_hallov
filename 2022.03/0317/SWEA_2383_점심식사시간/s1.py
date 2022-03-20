import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    stair = []
    people = []
    ans = 10000
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                people.append([i, j])
            elif arr[i][j] > 1:
                stair.append([arr[i][j], [i, j]])
    d_1, d_2 = [], []
    for i in range(2):
        sx, sy = stair[i][1]
        if not i:
            for person in people:
                x, y = person
                d = abs(sx - x) + abs(sy - y)
                d_1.append(d)
        else:
            for person in people:
                x, y = person
                d = abs(sx - x) + abs(sy - y)
                d_2.append(d)

    if len(people) == 1:
        test_1 = d_1[0] + stair[0][0]
        test_2 = d_2[0] + stair[1][0]
        ans = min(test_1, test_2)
        print(f'#{tc} {ans + 1}')
        continue

    people_idx = list(range(len(people)))
    for i in range(len(people) + 1):
        cases = combinations(people_idx, i)
        for case in cases:
            stair_1 = []
            stair_2 = []
            case = list(case)
            for idx in people_idx:
                if idx in case:
                    stair_1.append(d_1[idx])
                else:
                    stair_2.append(d_2[idx])
            stair_1.sort()
            stair_2.sort()
            time_1, time_2 = 0, 0
            now_stair_1 = []
            now_stair_2 = []
            while stair_1:
                if now_stair_1:
                    cnt = 0
                    for k in range(len(now_stair_1)):
                        now_stair_1[k] -= 1
                        if not now_stair_1[k]:
                            cnt += 1
                    for _ in range(cnt):
                        now_stair_1.remove(0)
                        stair_1.pop(0)
                for a in range(len(stair_1)):
                    if stair_1[a] > 0:
                        stair_1[a] -= 1
                    if not stair_1[a]:
                        if len(now_stair_1) < 3:
                            now_stair_1.append(stair[0][0])
                            stair_1[a] = -1
                time_1 += 1
                if time_1 > ans:
                    break
            while stair_2:
                if now_stair_2:
                    cnt = 0
                    for l in range(len(now_stair_2)):
                        now_stair_2[l] -= 1
                        if not now_stair_2[l]:
                            cnt += 1
                    for _ in range(cnt):
                        now_stair_2.remove(0)
                        stair_2.pop(0)
                for b in range(len(stair_2)):
                    if stair_2[b] > 0:
                        stair_2[b] -= 1
                    if not stair_2[b]:
                        if len(now_stair_2) < 3:
                            now_stair_2.append(stair[1][0])
                            stair_2[b] = -1
                time_2 += 1
                if time_2 > ans:
                    break
            ans = min(ans, max(time_1, time_2))

    print(f'#{tc} {ans + 1}')



