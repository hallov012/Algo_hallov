from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    idx = {}
    for i in range(n):
        idx[friends[i]] = i

    g = [[0] * n for _ in range(n)]
    send = [0] * n
    get = [0] * n

    for gift in gifts:
        a, b = gift.split()
        a_idx, b_idx = idx[a], idx[b]
        g[a_idx][b_idx] += 1
        send[a_idx] += 1
        get[b_idx] += 1

    cnt = [0] * n

    for i in range(n-1):
        for j in range(i+1, n):
            if g[i][j] > g[j][i]:
                cnt[i] += 1
            elif g[i][j] < g[j][i]:
                cnt[j] += 1
            else:
                i_point = send[i] - get[i]
                j_point = send[j] - get[j]
                if i_point > j_point:
                    cnt[i] += 1
                elif i_point < j_point:
                    cnt[j] += 1

    answer = max(cnt)

    return answer


data_lst = [
        [["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]],
        [["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]],
        [["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]]
        ]

for f, g in data_lst:
    print(solution(f, g))