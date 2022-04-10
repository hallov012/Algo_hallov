def counter(now, next):
    if now == 'N':
        if next == 'W':
            return 'right'
        elif next == 'E':
            return 'left'
    elif now == 'W':
        if next == 'N':
            return 'right'
        elif next == 'S':
            return 'left'
    elif now == 'S':
        if next == 'W':
            return 'right'
        elif next == 'E':
            return 'left'
    elif now == 'E':
        if next == 'S':
            return 'right'
        elif next == 'N':
            return 'left'

def solution(path):
    answer = []
    t = 0
    idx = 0
    n = len(path)
    while idx < n:
        flag = False
        for i in range(1, 6):
            if idx + i < n and path[idx + i] != path[idx]:
                flag = True
                next_path = counter(path[idx], path[idx + i])
                answer.append(f"Time {t}: Go straight {100 * i}m and turn {next_path}")
                idx += i
                t += i
                break
        if not flag:
            idx += 1
            t += 1
    return answer

print(solution('EEESEEEEEENNNN'))
print(solution('SSSSSSWWWNNNNNN'))