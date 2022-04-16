from itertools import combinations_with_replacement

def score(winner, challenger):
    scores = [0, 0]
    for i in range(11):
        if winner[i] == 0 and challenger[i] == 0:
            pass
        elif winner[i] > challenger[i]:
            scores[0] += 10 - i
        elif winner[i] <= challenger[i]:
            scores[1] += 10 - i

    return scores


def solution(n, info):
    answer = []
    flag = False
    visited = [0] * 11
    max_gap = 0
    nums = list(range(11))
    cases = list(combinations_with_replacement(nums, n))
    for case in cases:
        winners = [0] * 11
        for i in case:
            winners[i] += 1
        result = score(winners, info)
        if result[0] > result[1]:
            flag = True
            if max_gap < result[0] - result[1]:
                max_gap = result[0] - result[1]
                answer = [winners]
            elif max_gap == result[0] - result[1]:
                answer.append(winners)
    if not flag:
        return [-1]
    for i in range(10, -1, -1):
        max_cnt = 0
        max_lst = []
        for j in range(len(answer)):
            if answer[j][i] > max_cnt:
                max_cnt = answer[j][i]
                max_lst = [j]
            elif answer[j][i] == max_cnt:
                max_lst.append(j)
        if len(max_lst) == 1:
            return answer[max_lst[0]]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
