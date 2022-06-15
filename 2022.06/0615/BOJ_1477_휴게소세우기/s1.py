import sys
sys.stdin = open('input.txt')

n, m, l = map(int, input().split())
# 리스트의 양끝에 시작점, 끝점을 추가
service = [0] + list(map(int, input().split())) + [l]
service.sort()
start, end = 1, l-1 # 시작과 끝에는 휴게소를 건설할 수 없음
ans = 0
while start <= end:
    # mid => 휴게소가 없는 구간의 최댓값
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n+2):
        if service[i] - service[i-1] > mid:
            cnt += (service[i] - service[i-1] - 1) // mid
    # 최대 거리가 너무 짧다 => 더 넓은 간격으로 휴게소를 세워도 된다
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)