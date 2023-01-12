import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(range(n+1))

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])