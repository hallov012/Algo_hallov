from collections import deque

def solution(rc, operations):
    answer = [[]]
    rc = deque(rc)
    n = len(rc)
    m = len(rc[0])
    cnt = 0
    for oper in operations:
        if oper == 'ShiftRow':
            cnt += 1
        else:
            if cnt:
                for _ in range(cnt % n):
                    a = rc.pop()
                    rc.appendleft(a)
            cnt = 0
            save = rc[0][0]
            for j in range(m):
                if j != m-1:
                    s = rc[0][j+1]
                    rc[0][j+1] = save
                    save = s
                else:
                    s = rc[1][j]
                    rc[1][j] = save
                    save = s
            for i in range(1, n-1):
                s = rc[i + 1][m-1]
                rc[i + 1][m-1] = save
                save = s
            for j in range(m-1, -1, -1):
                if j != 0:
                    s = rc[n-1][j-1]
                    rc[n-1][j-1] = save
                    save = s
                else:
                    s = rc[n-2][j]
                    rc[n-2][j] = save
                    save = s
            for i in range(n-2, 1, -1):
                s = rc[i-1][0]
                rc[i-1][0] = save
                save = s
            rc[0][0] = save

    for _ in range(cnt % n):
        a = rc.pop()
        rc.appendleft(a)

    answer = list(rc)
    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))