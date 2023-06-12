import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], -x[0]))
ans = sys.maxsize
cnt = 0
temp = 0
same_w_flag = False
for i in range(n):
    w, c = meet[i]
    cnt += w
    # 이전과 같은 가격인 고기가 있다면 그 수를 temp에 저장
    if i > 0 and c == meet[i-1][1]:
        temp += 1
    else:
        temp = 0
    if cnt >= m:
        if temp == 0:
            ans = min(ans, c)
            break
        else:
            ans = min(ans, c * (temp+1))

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)