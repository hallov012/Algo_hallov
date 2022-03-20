import sys
sys.stdin = open('input.txt')

def fibo(num):
    global ans_zero, ans_one
    start = len(ans_zero)
    if num >= start:
        for i in range(start, num+1):
            ans_zero.append(ans_zero[i - 1] + ans_zero[i - 2])
            ans_one.append(ans_one[i - 1] + ans_one[i - 2])
    return

T = int(input())

for tc in range(T):
    n = int(input())
    ans_zero = [1, 0, 1]
    ans_one = [0, 1, 1]
    fibo(n)
    print(ans_zero[n], ans_one[n])