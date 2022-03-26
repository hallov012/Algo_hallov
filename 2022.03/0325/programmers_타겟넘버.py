from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    visited = [0] * n
    que = deque([[numbers[0], 0], [-1 * (numbers[0]), 0]])
    visited[0] = 1
    while que:
        cnt, idx = que.popleft()
        idx += 1
        if idx == n:
            if cnt == target:
                answer += 1
        else:
            que.append([cnt + numbers[idx], idx])
            que.append([cnt - numbers[idx], idx])
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))