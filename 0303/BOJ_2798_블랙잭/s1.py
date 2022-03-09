import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sub_set = []
ans = 0

def dfs():
    global ans
    if sum(sub_set) > m:
        return
    if len(sub_set) == 3:
        ans = max(ans, sum(sub_set))
        return
    for card in cards:
        if card not in sub_set:
            sub_set.append(card)
            dfs()
            sub_set.pop()

dfs()
print(ans)