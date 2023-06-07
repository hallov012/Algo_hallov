import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def transNum(char):
    return ord(char) - 65

x = int(input())
g = [[0] * 58 for _ in range(58)]
for _ in range(x):
    line = input().rsplit()
    a, b = line[0], line[2]
    g[transNum(a)][transNum(b)] = 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if g[i][k] and g[k][j]:
                g[i][j] = 1

ans = []
for i in range(58):
    for j in range(58):
        if i != j and g[i][j]:
            ans.append(f"{chr(i+65)} => {chr(j+65)}")

print(len(ans))
for x in ans:
    print(x)