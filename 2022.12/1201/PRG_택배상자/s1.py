def solution(order):
    answer = 0
    main = list(range(order[0], len(order)+1))
    sub = list(range(1, order[0]))
    for num in order:
        if main and main[0] == num:
            answer += 1
            main.pop(0)
        elif sub and sub[-1] == num:
            answer += 1
            sub.pop()
        else:
            break
    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))