import sys
sys.stdin = open('input.txt')

n = int(input())
rectangles = [list(map(int, input().split())) for _ in range(n)]


x, y = 0, 0
