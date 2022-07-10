"""
세그먼트 트리로 도전=> 실패
"""
import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        min_tree[node] = data[start]
        sum_tree[node] = data[start]
    else:
        mid = (start+end)//2
        min_tree[node] = min(init(node*2, start, mid)[0], init(node*2+1, mid+1, end)[0])
        sum_tree[node] = init(node*2, start, mid)[1] + init(node*2+1, mid+1, end)[1]
    print(min_tree[node], sum_tree[node])
    return (min_tree[node], sum_tree[node])

def find(node, start, end):
    if start == end:
        temp = min_tree

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

min_tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)
sum_tree = [0] * pow(2, math.ceil(math.log(n, 2))+1)

init(1, 0, n-1)



