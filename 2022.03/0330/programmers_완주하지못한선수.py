def solution(participant, completion):
    dic = {}
    for a in participant:
        if a not in dic.keys():
            dic[a] = 1
        else:
            dic[a] += 1
    for b in completion:
        dic[b] -= 1

    for key in dic.keys():
        if dic[key] != 0:
            answer = key
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))