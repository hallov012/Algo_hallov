from collections import deque

def solution(queue1, queue2):
    ans = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    for _ in range(300000):
        if q1_sum == q2_sum:
            return ans
        elif q1_sum > q2_sum:
            temp = q1.popleft()
            q2.append(temp)
            q1_sum -= temp
            q2_sum += temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            q2_sum -= temp
            q1_sum += temp
        ans += 1
    else:
        return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))