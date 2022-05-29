import sys
sys.stdin = open('input.txt')

# 아스키코드로 2차원 배열 만들기

input = sys.stdin.readline

word = input().strip()
m = len(word)
check = [[0] * m for _ in range(26)]
check[ord(word[0])-97][0] = 1
for i in range(1, m):
    check[ord(word[i])-97][i] = 1
    for j in range(26):
        check[j][i] += check[j][i-1]
q = int(input())
for _ in range(q):
    char, s, e = input().split()
    if int(s) > 0:
        print(check[ord(char)-97][int(e)] - check[ord(char)-97][int(s)-1])
    else:
        print(check[ord(char)-97][int(e)])
