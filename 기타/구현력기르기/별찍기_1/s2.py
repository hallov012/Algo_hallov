import sys
sys.stdin = open('input.txt')

T = int(input())

data = [[' ' for _ in range(T)] for _ in range(T)]
for i in range(T):
    for j in range(i+1):
        data[i][T-j-1] = '*'
for i in range(T):
    for j in range(T):
        print(data[i][j], end="")
    print()