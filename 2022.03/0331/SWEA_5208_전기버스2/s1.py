import sys
sys.stdin = open('input.txt')

def find(cnt, charge, idx):
    global ans
    if cnt >= ans:
        return
    if idx == n-1:
        ans = min(ans, cnt)
        return
    if charge - 1 >= 0: # 다음 정류장으로 갈 수 있는 경우
        find(cnt, charge - 1, idx + 1)
    find(cnt + 1, station[idx] - 1, idx + 1)


T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    n = data[0]
    station = data[1:]
    ans = n
    find(0, station[0] - 1, 1)
    print(f'#{tc} {ans}')