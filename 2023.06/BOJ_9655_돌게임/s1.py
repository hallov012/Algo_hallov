import sys
sys.stdin = open('input.txt')

n = int(input())
# 돌은 홀수로 가져갈 수 있음 => 돌이 홀수면 승리
if n % 2:
    print('SK')
else:
    print('CY')