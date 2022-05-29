import sys
sys.stdin = open('input.txt')

n = int(input())
result = [[0, []] for _ in range(n+1)]
result[1][0] = 0 # 횟수
result[1][1] = [1] # 경로

for i in range(2, n+1):
    result[i][0] = result[i-1][0] + 1
    result[i][1] = result[i-1][1] + [i]
    if not i % 3 and result[i//3][0] + 1 < result[i][0]:
        result[i][0] = result[i//3][0] + 1
        result[i][1] = result[i//3][1] + [i]
    if not i % 2 and result[i//2][0] + 1 < result[i][0]:
        result[i][0] = result[i//2][0] + 1
        result[i][1] = result[i//2][1] + [i]

print(result[n][0])
ans = result[n][1]
ans.reverse()
print(*ans)
