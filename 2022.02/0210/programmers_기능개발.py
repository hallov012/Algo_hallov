from collections import deque

def solution(progresses, speeds):
    answer = []
    now_work = progresses
    dq_speeds = deque(speeds)
    for _ in range(100):
        cnt = 0
        now_work = deque([now_work[i] + dq_speeds[i] for i in range(len(now_work))])
        if len(now_work) == 0:
            break
        else:
            if now_work[0] >= 100:
                cnt += 1
                now_work.popleft()
                dq_speeds.popleft()
                for _ in range(len(now_work)):
                    if now_work[0] >= 100:
                        cnt += 1
                        now_work.popleft()
                        dq_speeds.popleft()
                answer.append(cnt)
    return answer

        





print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# a = deque([1,2,3])
# b = deque([2, 2, 2])
# c = [a[i] + b[i] for i in range(len(a))]
# print(type(a))
# print(c, type(c))