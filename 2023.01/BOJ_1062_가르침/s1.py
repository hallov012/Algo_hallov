import sys
sys.stdin = open('input.txt')

def dfs(idx, cnt):
    global ans
    if cnt == k-5:
        temp = 0
        for word in words:
            for char in word:
                if not visited[ord(char)-97]:
                    break
            else:
                temp += 1
        ans = max(ans, temp)
    for i in range(idx+1, 26):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0

input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
know = {'a', 'n', 't', 'i', 'c'}
ans = 0
chars = set(chr(i) for i in range(97, 123)) - know
if k < 5:
    print(0)
    exit()

visited = [0] * 26
for char in know:
    visited[ord(char)-97] = 1

dfs(-1, 0)
print(ans)
