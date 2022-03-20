import sys
sys.stdin = open('input.txt')

n = int(input())
words = [input() for _ in range(n)]
ans = [[] for _ in range(51)]
for word in words:
    if word not in ans[len(word)]:
        ans[len(word)].append(word)
for i in range(51):
    if not ans[i]:
        pass
    elif len(ans[i]) == 1:
        print(ans[i][0])
    else:
        ans[i].sort()
        for j in range(len(ans[i])):
            print(ans[i][j])