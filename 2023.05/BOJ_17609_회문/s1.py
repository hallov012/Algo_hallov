import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    word = input().rstrip()
    left, right = 0, len(word)-1
    ans = 0
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if left <= right-1:
                temp = word[:right] + word[right+1:]
                if temp == temp[::-1]:
                    ans = 1
                    break
            if left+1 <= right:
                temp = word[:left] + word[left+1:]
                if temp == temp[::-1]:
                    ans = 1
                    break
            ans = 2
            break
    print(ans)