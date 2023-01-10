import sys
sys.stdin = open('input.txt')

c, p = map(int, input().split())
height = list(map(int, input().split()))
ans = 0
if p == 1:
    ans = c
    for i in range(c-3):
        if min(height[i:i+4]) == max(height[i: i+4]):
            ans += 1
if p == 2:
    for i in range(c-1):
        if height[i] == height[i+1]:
            ans += 1

if p == 3:
    for i in range(c-2):
        if height[i] == height[i+1] == height[i+2] - 1:
            ans += 1
    for i in range(c-1):
        if height[i] == height[i+1] + 1:
            ans += 1

if p == 4:
    for i in range(c-2):
        if height[i] == height[i+1] + 1 == height[i+2] + 1:
            ans += 1
    for i in range(c-1):
        if height[i] == height[i+1] - 1:
            ans += 1

if p == 5:
    for i in range(c-2):
        if min(height[i:i+3]) == max(height[i:i+3]) or height[i] == height[i+1] + 1 == height[i+2]:
            ans += 1
    for i in range(c-1):
        if height[i] == height[i+1] + 1 or height[i] == height[i+1] - 1:
            ans += 1

if p == 6:
    for i in range(c-2):
        if min(height[i: i+3]) == max(height[i: i+3]) or height[i] == height[i+1] - 1 == height[i+2] - 1:
            ans += 1
    for i in range(c-1):
        if height[i] == height[i+1] + 2 or height[i] == height[i+1]:
            ans += 1

if p == 7:
    for i in range(c-2):
        if min(height[i: i+3]) == max(height[i: i+3]) or height[i] == height[i+1] == height[i+2] + 1:
            ans += 1
    for i in range(c-1):
        if height[i] == height[i+1] - 2 or height[i] == height[i+1]:
            ans += 1


print(ans)