def solution(survey, choices):
    answer = ''
    test = ['RT', 'CF', 'JM', 'AN']
    score = [[0, 0] for _ in range(4)]
    n = len(survey)
    for i in range(n):
        a, b = survey[i][0], survey[i][1]
        num = choices[i]
        for j in range(4):
            if a in test[j]:
                q_idx = j
                a_idx = test[j].index(a)
                b_idx = test[j].index(b)
        if num <= 4:
            score[q_idx][a_idx] += 4 - num
        else:
            score[q_idx][b_idx] += num - 4

    for i in range(4):
        check = score[i]
        if check[0] >= check[1]:
            answer += test[i][0]
        else:
            answer += test[i][1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))