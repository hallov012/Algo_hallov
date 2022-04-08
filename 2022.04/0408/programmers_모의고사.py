def solution(answers):
    answer = []
    score = [0] * 3
    n = len(answers)
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        for j in range(n):
            if student[i][j % len(student[i])] == answers[j]:
                score[i] += 1
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))