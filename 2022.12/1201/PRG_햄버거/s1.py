def solution(ingredient):
    answer = 0
    stack = []
    for num in ingredient:
        stack.append(num)
        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                answer += 1
                for _ in range(4):
                    stack.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))