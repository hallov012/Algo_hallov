"""
정규식 => 난 모르겠다
* +:  앞에 붙은 요소가 최소 하나는 들어가야 한다
* (): 괄호 안의 요소들을 하나로 묶는다
* |: '또는'을 의미 한다 
"""
import sys, re
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    data = input().strip()
    check = re.compile('(100+1+|01)+')
    if check.fullmatch(data):
        print('YES')
    else:
        print('NO')