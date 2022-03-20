import sys
sys.stdin = open('input.txt')

n = int(input())
RGB = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])
print(min(RGB[n-1]))

# 이전에 칠한 색이 현재의 색과 다르면 되는 것이므로
# 현재 칠한 색을 제외한 다른 색들을 바로 직전 집에 칠했을 때의 최솟값에 그 금액을 더해주며
# 계속 갱신시킨다