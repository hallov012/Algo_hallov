def solution(dartResult):
    answer = 0
    result_lst = []
    score_lst = []
    i = 0
    while i < len(dartResult):
        if '0' <= dartResult[i] <= '9':
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                result_lst.append(int(10))
                i += 2
            else:
                result_lst.append(int(dartResult[i]))
                i += 1
        elif dartResult[i] in 'SDT':
            if dartResult[i] == 'S':
                answer += result_lst[-1]
                score_lst.append(result_lst[-1])
            elif dartResult[i] == 'D':
                answer += (result_lst[-1]) ** 2
                score_lst.append((result_lst[-1]) ** 2)
            else:
                answer += (result_lst[-1]) ** 3
                score_lst.append((result_lst[-1]) ** 3)
            i += 1
        else:
            if dartResult[i] == '*':
                if len(score_lst) == 1:
                    answer -= score_lst[-1]
                    score_lst.append(score_lst.pop() * 2)
                    answer += score_lst[-1]
                else:
                    answer -= score_lst[-1] + score_lst[-2]
                    b = score_lst.pop() * 2
                    a = score_lst.pop() * 2
                    score_lst.append(a)
                    score_lst.append(b)
                    answer += score_lst[-1] + score_lst[-2]
            elif dartResult[i] == '#':
                score_lst.append(-1 * score_lst.pop())
                answer += score_lst[-1] * 2
            i += 1
    return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1S*2T*3S"))
print(solution("1D2S0T"))

