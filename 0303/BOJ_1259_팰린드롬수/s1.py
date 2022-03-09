import sys
sys.stdin = open('input.txt')

while 1:
    nums = str(input())
    if nums == '0':
        break
    elif nums == nums[::-1]:
        print('yes')
    else:
        print('no')
