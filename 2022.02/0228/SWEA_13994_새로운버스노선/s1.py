import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 노선의 수
    data = [list(map(int, input().split())) for _ in range(n)]
    bus_type, start, end = [], [], []
    for i in range(n):
        bus_type.append(data[i][0])
        start.append(data[i][1])
        end.append(data[i][2])
    cnt = [0] * (max(end) + 1)
    for i in range(n):
        if bus_type[i] == 1:
            for j in range(start[i], end[i] +1):
                cnt[j] += 1
        elif bus_type[i] == 2:
            if start[i] % 2: # 시작이 홀수인 경우
                for j in range(start[i], end[i]+1, 2):
                    cnt[j] += 1
                if not end[i] % 2:
                    cnt[end[i]] += 1
            else:
                for j in range(start[i], end[i]+1, 2):
                    cnt[j] += 1
                if end[i] % 2:
                    cnt[end[i]] += 1
        else:
            if start[i] % 2: # 시작이 홀수 일 때 -> 3의 배수이면서 10의 배수가 아님
                for j in range(0, end[i]+1, 3):
                    if start[i] < j < end[i] and j % 30 != 0:
                        cnt[j] += 1
                cnt[start[i]] += 1
                cnt[end[i]] += 1
            else:
                for j in range(0, end[i]+1, 4):
                    if start[i] < j < end[i]:
                        cnt[j] += 1
                cnt[start[i]] += 1
                cnt[end[i]] += 1
    print(f'#{tc} {max(cnt)}')





