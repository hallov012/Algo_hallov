def solution(brown, yellow):
    answer = []
    yellow_sub = []
    for i in range(1, yellow+1):
        if not yellow % i:
            yellow_sub.append(i)
    for num in yellow_sub:
        num2 = yellow // num
        if 2*(num+2) + 2*(num2+2) - 4 == brown:
            answer = [num+2, num2+2]
    return answer

print(solution(10, 2))
print(solution(8, 1))