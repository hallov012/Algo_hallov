import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input()))
    cnt = [0] * (max(nums)+1)
    for num in nums:
        cnt[num] += 1
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            ans = i
    ans2 = max(cnt)
    print(f'#{tc} {ans} {ans2}')