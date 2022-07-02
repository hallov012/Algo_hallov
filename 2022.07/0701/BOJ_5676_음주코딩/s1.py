import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = data[start]
    else:
        tree[node] = init(node*2, start, (start+end)//2) * init(node*2+1, (start+end)//2+1, end)
    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = diff
    else:
        update(node*2, start, (start+end)//2, idx, diff)
        update(node*2+1, (start+end)//2+1, end, idx, diff)
        tree[node] = tree[node*2] * tree[node*2+1]

def multi(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    return multi(node*2, start, (start+end)//2, left, right) * multi(node*2+1, (start+end)//2+1, end, left, right)

input = sys.stdin.readline

while True:
    try:
        n, k = map(int, input().split())
        data = list(map(int, input().split()))
        for i in range(n):
            if data[i] > 0:
                data[i] = 1
            elif data[i] == 0:
                data[i] = 0
            else:
                data[i] = -1
        tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)
        init(1, 0, n-1)
        ans = ''
        for _ in range(k):
            a, b, c = map(str, input().split())
            if a == 'C':
                b, c = int(b)-1, int(c)
                if c > 0:
                    c = 1
                elif c == 0:
                    c = 0
                else:
                    c = -1
                data[b] = c
                update(1, 0, n-1, b, c)
            elif a == 'P':
                b, c = int(b)-1, int(c)-1
                temp = multi(1, 0, n-1, b, c)
                if temp > 0:
                    ans += '+'
                elif temp == 0:
                    ans += '0'
                else:
                    ans += '-'
        print(ans)

    except:
        break
