def solution(friends, gifts):
    n = len(friends)
    idx = {}
    for i in range(n):
        idx[friends[i]] = i

    g = [[0] * n for _ in range(n)]
    for gift in gifts:
        # 1이 준 사람, 2가 받은 사람
        name_1, name_2 = gift.split(' ')
        a, b = idx[name_1], idx[name_2]
        g[a][b] += 1
        g[b][a] -= 1

    score = [sum(g[i]) for i in range(n)]
    cnt = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            # 주고받은게 없거나, 똑같이 주고 받았을 때
            if g[i][j] == 0 and g[j][i] == 0:
                if score[i] > score[j]:
                    cnt[i] += 1
                elif score[i] < score[j]:
                    cnt[j] += 1
            else:
                if g[i][j] > g[j][i]:
                    cnt[i] += 1
                elif g[i][j] < g[j][i]:
                    cnt[j] += 1

    answer = max(cnt)
    return answer