import sys
sys.stdin = open('input.txt')

"""
위치 p
|ai - p| * bi들의 합이 최소가 되는 p를 구해야 한다
"""
n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
total = 0
