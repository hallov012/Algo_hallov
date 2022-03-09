import sys
sys.stdin = open('input.txt')

T = int(input())

data = []
for _ in range(T):
    num = int(sys.stdin.readline())
    data.append(num)

for i in range(T-1, 0, -1):
    for j in range(i):
        if data[j] > data[i]:
            data[j], data[i] = data[i], data[j]

for i in range(T):
    print(data[i])