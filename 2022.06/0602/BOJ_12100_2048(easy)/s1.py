import sys, copy
sys.stdin = open('input.txt')

def move(data, d):
    if d == 0:  # 오른쪽
        for i in range(n):
            end = n-1
            for j in range(n-2, -1, -1):
                if data[i][j]:
                    temp = data[i][j]
                    data[i][j] = 0
                    if data[i][end] == 0:
                        data[i][end] = temp
                    elif data[i][end] == temp:
                        data[i][end] = 2 * temp
                        end -= 1
                    else:
                        end -= 1
                        data[i][end] = temp
    elif d == 1: # 왼쪽
        for i in range(n):
            end = 0
            for j in range(1, n):
                if data[i][j]:
                    temp = data[i][j]
                    data[i][j] = 0
                    if data[i][end] == 0:
                        data[i][end] = temp
                    elif data[i][end] == temp:
                        data[i][end] = 2 * temp
                        end += 1
                    else:
                        end += 1
                        data[i][end] = temp
    elif d == 2: #아래쪽
        for j in range(n):
            end = n-1
            for i in range(n-2, -1, -1):
                if data[i][j]:
                    temp = data[i][j]
                    data[i][j] = 0
                    if data[end][j] == 0:
                        data[end][j] = temp
                    elif data[end][j] == temp:
                        data[end][j] = 2 * temp
                        end -= 1
                    else:
                        end -= 1
                        data[end][j] = temp
    else: #위쪽
        for j in range(n):
            end = 0
            for i in range(1, n):
                if data[i][j]:
                    temp = data[i][j]
                    data[i][j] = 0
                    if data[end][j] == 0:
                        data[end][j] = temp
                    elif data[end][j] == temp:
                        data[end][j] = 2 * temp
                        end += 1
                    else:
                        end += 1
                        data[end][j] = temp
    return data

def dfs(data, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, data[i][j])
        return
    for d in range(4):
        new_data = copy.deepcopy(data)
        temp_data = move(new_data, d)
        dfs(temp_data, cnt+1)

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(data, 0)
print(ans)