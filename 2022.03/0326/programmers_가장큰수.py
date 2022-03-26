def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return '0'
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    for char in numbers_str:
        answer += char
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0]))