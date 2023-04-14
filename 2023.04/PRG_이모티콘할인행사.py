def solution(users, emoticons):
    answer = [0, 0]
    n, m = len(emoticons), len(users)
    visited = [0] * n
    # 경우 체크
    def check():
        nonlocal answer
        cost = [0] * m
        for i in range(n):
            if visited[i]:
                for p in range(m):
                    if visited[i] >= users[p][0]:
                        cost[p] += emoticons[i] * (100 - visited[i]) // 100
        user_cnt, cost_cnt = 0, 0
        for p in range(m):
            if cost[p] >= users[p][1]:
                user_cnt += 1
            else:
                cost_cnt += cost[p]
        if user_cnt > answer[0]:
            answer = [user_cnt, cost_cnt]
        elif user_cnt == answer[0]:
            answer[1] = max(answer[1], cost_cnt)
        return

    def find(idx):
        if idx == n:
            check()
            return
        for i in range(5):
            visited[idx] = 10 * i
            find(idx+1)

    find(0)
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))