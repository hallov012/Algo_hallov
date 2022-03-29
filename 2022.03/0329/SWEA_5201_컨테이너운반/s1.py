import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    w_lst = list(map(int, input().split()))
    t_lst = list(map(int, input().split()))
    w_lst.sort(reverse=True)
    t_lst.sort(reverse=True)

    ans = 0
    visited = [0] * n
    for i in range(m):
        if i == n:  # 담을 수 있는 모든 화물에 대한 검색을 마친 것 으로 break를 한다.
            break
        for j in range(i, n):
            if t_lst[i] >= w_lst[j] and not visited[j]:
                visited[j] = 1
                ans += w_lst[j]
                break
    print(f'#{tc} {ans}')

