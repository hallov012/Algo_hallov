import sys
sys.stdin = open('input.txt')

def find_left(idx):
    slope = sys.maxsize
    cnt = 0
    for i in range(idx-1, -1, -1):
        temp = (data[idx] - data[i]) / (idx - i)
        if slope > temp:
            slope = temp
            cnt += 1
    return cnt

def find_right(idx):
    slope = -sys.maxsize
    cnt = 0
    for i in range(idx+1, n):
        temp = (data[idx]-data[i]) / (idx - i)
        if slope < temp:
            slope = temp
            cnt += 1
    return cnt

n = int(input())
data = list(map(int, input().split()))
ans = 0
for i in range(n):
    temp = find_left(i) + find_right(i)
    ans = max(ans, temp)
print(ans)
