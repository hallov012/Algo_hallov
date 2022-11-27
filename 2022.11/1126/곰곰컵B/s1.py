import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
dance = set(["ChongChong"])
for _ in range(n):
    a, b = input().rstrip().split()
    if a in dance:
        dance.add(b)
        continue
    if b in dance:
        dance.add(a)
print(len(dance))
