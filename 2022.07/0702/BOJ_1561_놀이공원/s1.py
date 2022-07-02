import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
time = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()
left, right = 0, 60000000000
t = 0
while left <= right:
    mid = (left + right) // 2
    # 일단 처음에 m명의 아이들이 탈 수 있음
    cnt = m
    for i in range(m):
        # mid라는 시간 동안 i번째 놀이기구에 몇명이 탈 수 있는지를 cnt에 더해줌
        cnt += mid // time[i]
    if cnt >= n:
        t = mid
        right = mid - 1
    else:
        left = mid + 1

# t-1 시간에 아이들이 몇 명 탑승했는지
cnt = m
for i in range(m):
    cnt += (t-1) // time[i]

# t 시간에 탑승한 놀이기구 찾기
for i in range(m):
    # t 시간에 마지막으로 탑승해서 모든 아이들 탑승이 완료된 것이므로 t는 time[i]의 배수
    if t % time[i] == 0:
        cnt += 1
    if cnt == n:
        print(i+1)
        break









