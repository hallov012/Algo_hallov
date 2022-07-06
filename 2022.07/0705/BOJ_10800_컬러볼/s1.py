import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
ball = []
for i in range(n):
    c, s = map(int, input().split())
    ball.append((c, s, i))
# 공의 크기 순으로 오름차순 정렬 (작은공 -> 큰공)
ball.sort(key=lambda x: x[1])
color_cnt = [0] * 200001
ans = [0] * n
total = 0

j = 0
for i in range(n):
    # i번째 공보다 작은 j번째 공의 크기, 색상 정보를 저장
    # ball[i]의 ans를 저장할 것이므로 해당 공보다 작은 ball[j]의 정보를 저장한다
    while ball[j][1] < ball[i][1]:
        color_cnt[ball[j][0]] += ball[j][1]
        # i번째 공보다 작은 모든 공의 크기의 합 total
        total += ball[j][1]
        j += 1
    # total - ball[i]와 같은 색이고 더 작은 공의 크기의 합
    ans[ball[i][2]] = total - color_cnt[ball[i][0]]

for num in ans:
    print(num)
