import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    words = list(map(str, input().strip().split(' ')))
    print(f'Case #{tc}:', end=' ')
    for i in range(len(words)-1, -1, -1):
        if i == 0:
            print(words[i], end='')
        else:
            print(words[i], end=' ')
    print()
