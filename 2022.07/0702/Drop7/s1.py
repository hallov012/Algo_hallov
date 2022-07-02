import sys
sys.stdin = open('input.txt')



input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(7)]
n = int(input())