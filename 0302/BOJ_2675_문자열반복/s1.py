import sys
sys.stdin = open('input.txt')

n = int(input())

for tc in range(n):
    r, word = map(str, input().split())
    R = int(r)
    for char in word:
        print(char * R, end='')
    print()