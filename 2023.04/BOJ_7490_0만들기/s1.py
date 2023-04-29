import sys
sys.stdin = open('input.txt')

def calc(temp):
    temp = temp.replace(' ', '')
    if eval(temp):
        return False
    else:
        return True

def find(now ,temp):
    if now == n:
        temp += str(now)
        if calc(temp):
            print(temp)
        return
    find(now+1, temp + str(now) + ' ')
    find(now+1, temp + str(now) + '+')
    find(now+1, temp + str(now) + '-')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    find(1, '')
    print()