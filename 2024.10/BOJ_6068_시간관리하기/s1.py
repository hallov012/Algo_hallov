import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
works.sort(key=lambda x:x[1])

ans = works[0][1] - works[0][0]
idx, save = 1, 0
while ans >= 0 and idx < n:
    last = works[idx-1][1]
    t, s = works[idx]
    if last + t < s:
        save += s - last - t
    else:
        save -= last + t - s
        if save < 0:
            ans += save
            save = 0
    idx += 1

print(ans if idx == n else -1)