def solution(s):
    answer = ''
    cnt = 0
    stack = ''
    for char in s:
        if char == ' ':
            if stack != '' and cnt == 0:
                for i in range(len(stack)):
                    if i % 2:
                        answer += stack[i].lower()
                    else:
                        answer += stack[i].upper()
            stack = ''
            cnt += 1
        else:
            if cnt != 0:
                answer += ' ' * cnt
                cnt = 0
            stack += char
    if stack != '':
        for i in range(len(stack)):
            if i % 2:
                answer += stack[i].lower()
            else:
                answer += stack[i].upper()
    if cnt != 0:
        answer += ' ' * cnt
    return answer

print(solution("try  hello world"))