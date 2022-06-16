import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]
start = min(time)
end = max(time) * m
ans = max(time) * m
while start <= end:
    cnt = 0
    mid = (start + end)//2
    for i in range(n):
        # 한 직원이 mid time동안 검사할 수 있는 인원의 수를 카운트
        cnt += mid // time[i]
    if cnt >= m:
        end = mid - 1
        ans = min(ans, mid)
    else:
        start = mid + 1
print(ans)
