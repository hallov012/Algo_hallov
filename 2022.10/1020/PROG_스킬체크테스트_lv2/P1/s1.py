def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        s = bin(s.count('1'))[2:]
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))