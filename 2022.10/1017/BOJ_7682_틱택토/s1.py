import sys
sys.stdin = open('input.txt')

def find():
    flag = [[0] * 4 for _ in range(2)]
    # 가로 판별
    for i in range(3):
        count = [0, 0]
        for j in range(3):
            if arr[i][j] == 'X':
                count[0] += 1
            elif arr[i][j] == 'O':
                count[1] += 1
        if count[0] == 3:
            flag[0][0] += 1
        if count[1] == 3:
            flag[1][0] += 1

    # 세로 판별
    for j in range(3):
        count = [0, 0]
        for i in range(3):
            if arr[i][j] == 'X':
                count[0] += 1
            elif arr[i][j] == 'O':
                count[1] += 1
        if count[0] == 3:
            flag[0][1] += 1
        if count[1] == 3:
            flag[1][1] += 1

    # 대각선 판별
    count = [0, 0]
    for i in range(3):
        if arr[i][i] == 'X':
            count[0] += 1
        elif arr[i][i] == 'O':
            count[1] += 1
    if count[0] == 3:
        flag[0][2] += 1
    if count[1] == 3:
        flag[1][2] += 1

    count = [0, 0]
    for i in range(3):
        if arr[i][2-i] == 'X':
            count[0] += 1
        elif arr[i][2-i] == 'O':
            count[1] += 1
    if count[0] == 3:
        flag[0][3] += 1
    if count[1] == 3:
        flag[1][3] += 1
    return flag

input = sys.stdin.readline

while True:
    data = input().rstrip()
    if data == 'end':
        break
    arr = [[] for _ in range(3)]
    for i in range(3):
        for j in range(i*3, (i+1)*3):
            arr[i].append(data[j])
    if data.count('X') == data.count('O') or data.count('X') == data.count('O') + 1:
        pass
    else:
        print('invalid')
        continue
    cnt = data.count('X') + data.count('O')
    # 만약 cnt가 짝수라면(2번이 마지막으로 진행한 경우) 2번이 승리해야 한다.
    # 하지만 초기 상태에서 가로나 세로에서 2줄씩 빙고가 나온 경우 그 게임은 오류가 있는 것 이므로 invalid를 출력해야함
    ans = False
    flag = find()
    if cnt % 2:
        if sum(flag[0]):
            if not sum(flag[1]):
                if max(flag[0]) == 1:
                    print('valid')
                else:
                    print('invalid')
            else:
                print('invalid')
        else:
            if cnt == 9:
                if not sum(flag[1]):
                    print('valid')
                else:
                    print('invalid')
            else:
                print('invalid')
    else:
        if sum(flag[1]):
            if not sum(flag[0]):
                if max(flag[1]) == 1:
                    print('valid')
                else:
                    print('invalid')
            else:
                print('invalid')
        else:
            print('invalid')