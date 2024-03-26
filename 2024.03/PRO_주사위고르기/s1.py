from itertools import combinations

def solution(dice):
    answer = []
    n = len(dice)
    cases = combinations(list(range(n)), n//2)
    sub_sums = []
    for d in dice:
        sub_sum = [0] * 101
        for k in d:
            sub_sum[k] += 1
        for i in range(2, 101):
            sub_sum[i] += sub_sum[i-1]
        sub_sums.append(sub_sum)

    cnt = {}
    total = 6**(n)
    print(total)
    for case in cases:
        if cnt.get(case):
            continue
        win = 0


    return answer

datas = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
]

for data in datas:
    print(solution(data))