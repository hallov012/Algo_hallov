from collections import deque

def solution(queue1, queue2):
    answer = 0
    total = sum(queue1) + sum(queue2)
    mid = total // 2
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    que_1 = deque(queue1)
    que_2 = deque(queue2)
    while sum_1 != sum_2:
        if sum_1 > mid:
            a = que_1.popleft()
            sum_1 -= a
            que_2.append(a)
            sum_2 += a
            answer += 1
        if sum_2 > mid:
            a = que_2.popleft()
            sum_2 -= a
            que_1.append(a)
            sum_1 += a
            answer += 1
        if answer > 3 * len(queue1):
            answer = -1
            break

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
print(solution([3],[1]))