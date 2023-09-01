import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def find(cnt, l, r):
    global ans
    if cnt > 3:
        return
    if l >= r:
        ans = min(ans, cnt)
        return
    if word[l] != word[r]:
        # 왼쪽만 삭제, 오른쪽만 삭제, 양쪽 다 삭제
        find(cnt+1, l+1, r)
        find(cnt+1, l, r-1)
        find(cnt+2, l+1, r-1)
    else:
        find(cnt, l+1, r-1)

word = input()
n = len(word)
ans = 4
find(0, 0, n-1)
print(ans if ans != 4 else -1)
