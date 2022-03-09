import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
f_lst = [0] * 6
m_lst = [0] * 6
for i in range(n):
    student = list(map(int, input().split()))
    if not student[0]:
        f_lst[student[1]-1] += 1
    else:
        m_lst[student[1]-1] += 1
ans = 0
for i in range(6):
    if 0 < f_lst[i] <= k:
        ans += 1
    elif not f_lst[i] % k:
        ans += f_lst[i] // k
    elif f_lst[i] // k > 0 and f_lst[i] % k > 0:
        ans += (f_lst[i] // k) + 1
    if 0 < m_lst[i] <= k:
        ans += 1
    elif not m_lst[i] % k:
        ans += m_lst[i] // k
    elif m_lst[i] // k > 0 and m_lst[i] % k > 0:
        ans += (m_lst[i] // k) + 1
print(ans)