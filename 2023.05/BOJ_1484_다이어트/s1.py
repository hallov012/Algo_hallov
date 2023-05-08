import sys
sys.stdin = open('input.txt')

g = int(input())
# left: 현재, right: 기억
left, right = 1, 1
ans = []
while True:
    temp = (left + right) * (left - right)
    if left == right+1 and temp > g:
        break
    if temp == g:
        ans.append(left)
        left += 1
    elif temp < g:
        left += 1
    else:
        right += 1
if ans:
    print(*ans, sep='\n')
else:
    print(-1)
