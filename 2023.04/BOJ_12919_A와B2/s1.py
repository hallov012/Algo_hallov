import sys
sys.stdin = open('input.txt')

def find(s):
    global ans
    if len(s) == len(S):
        if s == S:
            ans = 1
        return
    if s[0] == 'B':
        s.reverse()
        s.pop()
        find(s)
        s.append('B')
        s.reverse()
    if s[-1] == 'A':
        s.pop()
        find(s)
        s.append('A')


S = list(input())
T = list(input())
ans = 0
find(T)
print(ans)
