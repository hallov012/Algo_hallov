import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

sub_set = []

def dfs():
    if len(sub_set) == m:
        print(*sub_set)
        return
    for i in range(1, n+1):
        sub_set.append(i)
        dfs()
        sub_set.pop()

dfs()