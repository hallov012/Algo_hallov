import sys
sys.stdin = open('input.txt')

n = int(input())
word = input()
if len(set(word)) <= n:
    print(len(word))
    exit()

left, right = 0, 1
temp = set()
temp.add(word[0])
ans = 0
while left <= right:
    if right == len(word):
        ans = max(ans, right - left)
        break
    temp.add(word[right])
    if len(temp) == n:
        ans = max(ans, right - left + 1)
        right += 1
    elif len(temp) > n:
        temp = set()
        left += 1
        right = left + 1
        temp.add(word[left])
    else:
        right += 1

print(ans)