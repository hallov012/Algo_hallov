import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    cnt = [0] * (n+1)
    for i in submit:
        cnt[i] += 1
    not_submit = []
    for i in range(1, n+1):
        if not cnt[i]:
            not_submit.append(i)
    print(f'#{tc}', end=" ")
    print(*sorted(not_submit))