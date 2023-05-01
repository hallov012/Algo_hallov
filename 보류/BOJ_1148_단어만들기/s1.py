import sys
from collections import defaultdict

sys.stdin = open('input.txt')
words = []
while True:
    word = input().rstrip()
    if word == '-':
        break
    words.append(word)
cases = []
while True:
    case = input().rstrip()
    if case == '#':
        break
    cases.append(case)

for case in cases:
    dic = {}
    for char in case:
        dic[char] = 0
        for word in words:
            if char in word:

