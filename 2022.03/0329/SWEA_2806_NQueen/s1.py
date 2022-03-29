import sys
sys.stdin = open('input.txt')

def find(data, cnt):
    global ans
    if cnt == n:
        ans += 1
        return
    m = len(data)
    for j in range(n):
        if not data:
            data.append(j)
            find(data, cnt + 1)
            data.pop()
        else:
            if j not in data:        # 이미 그 열에 퀸이 있다면 놓을 수 없음
                check = True         # 대각선 검사를 해서 모든 경우에 pass 해야 함
                for k in range(m):   # 대각선 검사
                    if j in [data[k] - (cnt-k), data[k] + (cnt-k)]:
                        check = False
                        break
                if check:
                    data.append(j)
                    find(data, cnt + 1)
                    data.pop()

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = 0
    find([], 0)
    print(f'#{tc} {ans}')


