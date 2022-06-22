"""
bisect 모듈 사용
bisect_left(a, x): 정렬된 a에 x를 삽입할 위치를 리턴, x가 이미 a에 있다면 기존 항목의 앞(왼쪽) 위치 반환
bisect_right(a, x): 위와 동일, 하지만 기존 항목의 뒤(오른쪽) 위치 반환
https://folivora.tistory.com/83
기존 2,3번 문제에 memorization의 index를 저장하는 새로운 리스트 생성
"""
import sys
from bisect import bisect_left
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
memorization = [0]
idx = [0] * (n+1)
for i in range(n):
    num = nums[i]
    if memorization[-1] < num:
        memorization.append(num)
        idx[i] = len(memorization) - 1
    else:
        idx[i] = bisect_left(memorization, num)
        memorization[idx[i]] = num

ans = len(memorization) - 1
print(ans)
ans_lst = []
for i in range(n, -1, -1):
    if idx[i] == ans:
        ans_lst.append(nums[i])
        ans -= 1
print(*reversed(ans_lst))