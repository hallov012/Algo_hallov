def solution(alp, cop, problems):
    answer = 0
    n = len(problems)
    cnt = 0
    problems.sort(key=lambda x: (x[0], x[1], -x[4]))
    while cnt != n:
        now_p = problems[cnt]
        if alp >= now_p[0] and cop >= now_p[1]:
            answer += now_p[4]
            alp += now_p[2]
            cop += now_p[3]
            cnt += 1
        else:
            if cnt == 0:
                if alp < now_p[0]:
                    answer += now_p[0] - alp
                    alp = now_p[0]
                if cop < now_p[1]:
                    answer += now_p[1] - cop
                    cop = now_p[1]
            else:
                answer += problems[cnt-1][4]
                alp += problems[cnt-1][2]
                cop += problems[cnt-1][3]


    return answer

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))