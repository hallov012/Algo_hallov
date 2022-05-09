import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[int(input())] += 1
sort_dic = sorted(dic.items())
for key, value in sort_dic:
    for _ in range(value):
        print(key)