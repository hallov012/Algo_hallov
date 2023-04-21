def solution(survey, choices):
    answer = ''
    cnt = {}
    for char in 'RTFCMJAN':
        cnt[char] = 0
    n = len(survey)

    for i in range(n):
        s = survey[i]
        c = choices[i]
        if c < 4:
            cnt[s[0]] += abs(c-4)
        else:
            cnt[s[1]] += abs(c-4)
    cases = ['RT', 'CF', 'JM', 'AN']
    for case in cases:
        temp = 0
        if cnt[case[0]] >= cnt[case[1]]:
            answer += case[0]
        else:
            answer += case[1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))