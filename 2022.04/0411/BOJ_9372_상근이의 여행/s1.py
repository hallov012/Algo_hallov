import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
    print(n-1)
    # 모든 국가가 연결되어 있으므로 무조건 n다-1이 최소가 된