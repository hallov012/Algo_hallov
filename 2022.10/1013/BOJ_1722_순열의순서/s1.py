import sys
sys.stdin = open('input.txt')

n = int(input())
c, *arr = map(int, input().split())
if c == 1:
    cnt = 0
    ans = []
    visited = [0] * (n+1)
    while len(ans) != n:
        for i in range(1, n+1):
            if not visited[i]:
                temp = 1
                for j in range(1, n-len(ans)):
                    temp *= j
                if cnt + temp >= arr[0]:
                    ans.append(i)
                    visited[i] = 1
                    break
                else:
                    cnt += temp
    print(*ans)

if c == 2:
    ans = 0
    visited = [0] * (n+1)
    while arr:
        num = arr.pop(0)
        temp = 1
        cnt = 0
        visited[num] = 1
        for i in range(1, num):
            if not visited[i]:
                cnt += 1
        for i in range(1, len(arr)+1):
            temp *= i
        ans += cnt * temp
    print(ans+1)


