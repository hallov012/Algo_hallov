import sys
sys.stdin = open('input.txt')

n = int(input())
cnt = 0
num = 665
while cnt < n:
    num += 1
    if '666' in str(num):
        cnt += 1
print(num)
