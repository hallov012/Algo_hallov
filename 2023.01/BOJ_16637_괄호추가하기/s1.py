import sys
sys.stdin = open('input.txt')

def nums_oper(a, b, oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b

def dfs(idx, cnt):
    global ans
    if idx == n-1:
        ans = max(ans, cnt)
    if idx + 2 < n:
        dfs(idx + 2, nums_oper(cnt, int(s[idx + 2]), s[idx + 1]))
    if idx + 4 < n:
        next = nums_oper(int(s[idx+2]), int(s[idx+4]), s[idx+3])
        dfs(idx + 4, nums_oper(cnt, next, s[idx+1]))

n = int(input())
s = input().rstrip()
ans = -sys.maxsize
dfs(0, int(s[0]))
print(ans)



