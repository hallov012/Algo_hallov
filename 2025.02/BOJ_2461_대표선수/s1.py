import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
c_lst = [sorted(list(map(int, input().split()))) for _ in range(n)]

