def solution(N, stages):
    answer = []
    now_player = [0] * (N+2)
    for i in stages:
        now_player[i] += 1
    arrive_player = [0] * (N+2)
    for i in range(N+2):
        arrive_player[i] = sum(now_player[i:])
    clear_player = [0] * (N+2)
    for i in range(N+1):
        clear_player[i] = arrive_player[i] - now_player[i]
    d_rate = [0] * (N+2)
    for i in range(N+2):
        if now_player[i] != 0 and arrive_player[i] != 0:
            d_rate[i] = now_player[i] / arrive_player[i]
    d_rate = d_rate[1:N+1]
    stages_lst = list(range(1, N+1))
    dic = dict(zip(stages_lst, d_rate))
    sort_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    for i in range(len(sort_dic)):
        answer.append(sort_dic[i][0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))