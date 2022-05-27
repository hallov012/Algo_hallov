import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    word = input().strip()
    check = defaultdict(int)
    check[word[0]] += 1
    flag = True
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            pass
        else:
            if check[word[i]]:
                flag = False
                break
            else:
                check[word[i]] += 1
    if flag:
        ans += 1
print(ans)

