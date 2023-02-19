import sys
sys.stdin = open('input.txt')

def dfs(temp, cnt):
    global max_ans, min_ans
    if cnt == n+1:
        if min_ans == '':
            min_ans = temp
        else:
            max_ans = temp
        return
    if cnt == 0:
        for i in range(10):
            visited[i] = True
            dfs(str(i), 1)
            visited[i] = False
    else:
        if orders[cnt-1] == '>':
            for i in range(int(temp[-1])):
                if not visited[i]:
                    visited[i] = True
                    dfs(temp+str(i), cnt+1)
                    visited[i] = False
        else:
            for i in range(int(temp[-1]), 10):
                if not visited[i]:
                    visited[i] = True
                    dfs(temp+str(i), cnt+1)
                    visited[i] = False

n = int(input())
orders = list(map(str, input().split()))
nums = list(range(10))
visited = [0] * 10
max_ans = ''
min_ans = ''
dfs('', 0)
print(max_ans)
print(min_ans)

