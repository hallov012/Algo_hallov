import sys
sys.stdin = open('input.txt')

n = int(input())
word = input()
if len(word) == 1:
    print(1)
    exit()
elif len(set(word)) <= n:
    print(len(word))
    exit()

left, right = 0, 1
part = set()
part.add(word[0])
ans = 0
while left < len(word)-1:
    if right == len(word):
        ans = max(ans, right-left)
        break
    part.add(word[right])
    if len(part) == n:
        ans = max(ans, right-left+1)
        right += 1
    elif len(part) > n:
        part.clear()
        left += 1
        part.add(word[left])
        right = left + 1
    else:
        right += 1

print(ans)