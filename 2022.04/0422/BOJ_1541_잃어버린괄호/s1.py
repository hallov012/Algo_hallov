import sys
sys.stdin = open('input.txt')

words = input()
my_list = []
stack = ''
for char in words:
    if char not in '+-':
        stack += char
    else:
        my_list.append(int(stack))
        stack = ''
        my_list.append(char)
my_list.append(int(stack))
plus_list = []
i = 0
while i < len(my_list):
    if my_list[i] == '+':
        a = plus_list.pop()
        plus_list.append(a+my_list[i+1])
        i += 2
    elif my_list[i] == '-':
        i += 1
    else:
        plus_list.append(my_list[i])
        i += 1

ans = plus_list[0]
for i in range(1, len(plus_list)):
    ans -= plus_list[i]
print(ans)
