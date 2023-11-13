import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n = int(input())
nickname_dict = defaultdict(int)
for _ in range(n):
    nickname = input().rstrip()
