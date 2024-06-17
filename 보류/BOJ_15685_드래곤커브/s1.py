import sys
sys.stdin = open('input.txt')

n = int(input())
curve = [tuple(map(int, input().split())) for _ in range(n)]
