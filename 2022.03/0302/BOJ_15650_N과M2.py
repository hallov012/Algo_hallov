import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

sub_set = []
ans = []

def dfs():
    if len(sub_set) == m:
        if sorted(sub_set) not in ans:
            ans.append(sorted(sub_set))
        return
    for i in range(1, n+1):
        if i not in sub_set:
            sub_set.append(i)
            dfs()
            sub_set.pop()

dfs()
for i in range(len(ans)):
    print(*ans[i])