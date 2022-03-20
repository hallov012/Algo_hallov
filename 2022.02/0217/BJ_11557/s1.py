import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    t = int(input())
    uni = []
    alcol = []
    max_a = 0
    for i in range(t):
        data = list(sys.stdin.readline().split())
        uni.append(data[0])
        alcol.append(int(data[1]))
    my_dic = dict(zip(uni, alcol))
    for i in range(t):
        if alcol[i] > max_a:
            max_a = alcol[i]
    for key,value in my_dic.items():
        if value == max_a:
            print(key)


